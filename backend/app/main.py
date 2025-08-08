from fastapi import FastAPI
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from app.database import Base, engine, SessionLocal
from app.routes import users, sheets, rows
from app.models import User

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Создание пользователя admin при первом запуске
def create_default_admin():
    db: Session = SessionLocal()
    existing_admin = db.query(User).filter(User.username == "admin").first()
    if not existing_admin:
        admin_user = User(
            username="admin",
            hashed_password=bcrypt.hash("admin"),
            role="admin"
        )
        db.add(admin_user)
        db.commit()
        print("✅ Admin user created: admin/admin")
    else:
        print("ℹ️ Admin user already exists")
    db.close()

create_default_admin()

# Инициализация FastAPI
app = FastAPI(title="Mini Excel API")

# Подключение маршрутов
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(sheets.router, prefix="/api/sheets", tags=["Sheets"])
app.include_router(rows.router, prefix="/api/rows", tags=["Rows"])
