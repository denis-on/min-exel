from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Sheet(Base):
    __tablename__ = "sheets"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

class SheetPermission(Base):
    __tablename__ = "sheet_permissions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    sheet_id = Column(Integer, ForeignKey("sheets.id"))
    access_level = Column(String, nullable=False)

class SheetColumn(Base):
    __tablename__ = "sheet_columns"
    id = Column(Integer, primary_key=True)
    sheet_id = Column(Integer, ForeignKey("sheets.id"))
    name = Column(String, nullable=False)
    position = Column(Integer, nullable=False)

class SheetRow(Base):
    __tablename__ = "sheet_rows"
    id = Column(Integer, primary_key=True)
    sheet_id = Column(Integer, ForeignKey("sheets.id"))
    data = Column(JSON, nullable=False)
    version = Column(Integer, default=1)
    updated_by = Column(Integer, ForeignKey("users.id"))
    updated_at = Column(DateTime, default=datetime.utcnow)
