#!/usr/bin/env python3
"""
AICTE APAAR ID-Based Student Data Management Platform
Automated Database Seed Script (PostgreSQL + SQLAlchemy)
--------------------------------------------------------
Populates:
1. 3 Institutions (Madras Institute of Tech, CEG Anna Univ, PSG Tech)
2. 20+ Students covering:
   - Valid records matching approved intake
   - Duplicate APAAR ID alerts across colleges
   - Intake Breach Warning (PSG College: 95 enrolled vs 90 approved)
   - Missing/Truncated APAAR ID Warnings
3. Access Audit Logs with real-time verification alerts
"""

import os
import uuid
import datetime
from sqlalchemy import create_engine, Column, String, Integer, Boolean, DateTime, ForeignKey, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/aicte_apaar")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Institution(Base):
    __tablename__ = "institutions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    aicte_id = Column(String(50), unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    state = Column(String(100), nullable=False)
    approved_intake = Column(Integer, nullable=False)

class Student(Base):
    __tablename__ = "students"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    apaar_id = Column(String(12), nullable=False, index=True)
    student_id = Column(String(100), nullable=False)
    full_name = Column(String(255), nullable=False)
    program = Column(String(100), nullable=False)
    admission_year = Column(Integer, nullable=False)
    admission_category = Column(String(50), nullable=False)
    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"), nullable=False)
    validation_status = Column(String(50), default="Pending")
    validation_notes = Column(String)

class AccessAuditLog(Base):
    __tablename__ = "access_audit_logs"
    log_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    apaar_id = Column(String(12), nullable=False, index=True)
    verifier_entity = Column(String(255), nullable=False)
    access_timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    ip_address = Column(String(45), nullable=False)
    alert_dispatched = Column(Boolean, default=False)

def seed():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()

    print("[*] Clearing existing tables...")
    session.query(AccessAuditLog).delete()
    session.query(Student).delete()
    session.query(Institution).delete()

    print("[*] Seeding AICTE-Approved Institutions...")
    mit = Institution(
        id=uuid.UUID("a0000000-0000-0000-0000-000000000001"),
        aicte_id="AICTE-TN-042",
        name="Madras Institute of Technology, Chennai",
        state="Tamil Nadu",
        approved_intake=120
    )
    ceg = Institution(
        id=uuid.UUID("a0000000-0000-0000-0000-000000000002"),
        aicte_id="AICTE-TN-001",
        name="College of Engineering Guindy, Anna University",
        state="Tamil Nadu",
        approved_intake=180
    )
    psg = Institution(
        id=uuid.UUID("a0000000-0000-0000-0000-000000000003"),
        aicte_id="AICTE-TN-015",
        name="PSG College of Technology, Coimbatore",
        state="Tamil Nadu",
        approved_intake=90
    )
    session.add_all([mit, ceg, psg])
    session.flush()

    print("[*] Seeding Students (Valid, Duplicate, Warnings)...")
    # Valid records for MIT
    session.add(Student(
        apaar_id="123456789012", student_id="MIT-2026-CSE-001", full_name="Aarav Ramanathan",
        program="B.Tech Computer Science & Engineering", admission_year=2026, admission_category="Regular",
        institution_id=mit.id, validation_status="Valid", validation_notes="Verified: 12-digit APAAR valid"
    ))
    session.add(Student(
        apaar_id="234567890123", student_id="MIT-2026-CSE-002", full_name="Kavya Sundaram",
        program="B.Tech Computer Science & Engineering", admission_year=2026, admission_category="Regular",
        institution_id=mit.id, validation_status="Valid", validation_notes="Verified: 12-digit APAAR valid"
    ))

    # Duplicate APAAR ID across MIT and CEG
    duplicate_apaar = "548291037462"
    session.add(Student(
        apaar_id=duplicate_apaar, student_id="MIT-2026-IT-022", full_name="Siddharth Natarajan",
        program="B.Tech Information Technology", admission_year=2026, admission_category="Regular",
        institution_id=mit.id, validation_status="Duplicate",
        validation_notes="DUPLICATE ALERT: Registered at MIT and CEG simultaneously"
    ))
    session.add(Student(
        apaar_id=duplicate_apaar, student_id="CEG-2026-CSE-091", full_name="Siddharth Natarajan",
        program="B.Tech Computer Science & Engineering", admission_year=2026, admission_category="Regular",
        institution_id=ceg.id, validation_status="Duplicate",
        validation_notes="DUPLICATE ALERT: Registered at CEG and MIT simultaneously"
    ))

    # Format Warning (10 digits)
    session.add(Student(
        apaar_id="8839201948", student_id="MIT-2026-ECE-031", full_name="Varun Swaminathan",
        program="B.Tech Electronics & Communication", admission_year=2026, admission_category="Regular",
        institution_id=mit.id, validation_status="Warning",
        validation_notes="FORMAT ERROR: APAAR ID must be 12 digits (found 10 digits)"
    ))

    # Seeding PSG with 95 students to trigger Capacity Exceeded breach (95 > 90)
    for i in range(1, 96):
        is_excess = i > 90
        session.add(Student(
            apaar_id=f"9100{i:04d}{1000 + i}",
            student_id=f"PSG-2026-ENG-{i:03d}",
            full_name=f"PSG Student {i}",
            program="B.Tech Mechanical Engineering" if i <= 50 else "B.Tech Robotics and Automation",
            admission_year=2026,
            admission_category="Regular",
            institution_id=psg.id,
            validation_status="Valid",
            validation_notes="INTAKE EXCEEDED" if is_excess else "Verified: 12-digit APAAR valid"
        ))

    # Seed Sample Audit Logs
    session.add(AccessAuditLog(
        apaar_id="123456789012",
        verifier_entity="Tata Consultancy Services (TCS) Campus Verification Desk",
        ip_address="14.143.190.45",
        alert_dispatched=True
    ))

    session.commit()
    print("[+] Seeding successfully completed! Database is fully populated.")

if __name__ == "__main__":
    seed()
