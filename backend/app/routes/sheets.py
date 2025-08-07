from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_db, get_current_user
from app.models import Sheet
from app.schemas import SheetCreate

router = APIRouter()

@router.post("/")
def create_sheet(sheet: SheetCreate, user = Depends(get_current_user), db: Session = Depends(get_db)):
    if user.role != "admin":
        raise HTTPException(status_code=403)
    new_sheet = Sheet(name=sheet.name, created_by=user.id)
    db.add(new_sheet)
    db.commit()
    return new_sheet
