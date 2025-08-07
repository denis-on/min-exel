from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_db, hash_password, verify_password, create_token, get_current_user
from app.models import User
from app.schemas import UserCreate

router = APIRouter()

@router.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=401)
    token = create_token({"sub": user.id})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/")
def create_user(user: UserCreate, current: User = Depends(get_current_user), db: Session = Depends(get_db)):
    if current.role != "admin":
        raise HTTPException(status_code=403)
    new_user = User(username=user.username, password_hash=hash_password(user.password), role=user.role)
    db.add(new_user)
    db.commit()
    return new_user
