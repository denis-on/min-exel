from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth import get_db, get_current_user
from app.models import SheetRow
from app.schemas import RowUpdate
from datetime import datetime

router = APIRouter()

@router.put("/{row_id}")
def update_row(row_id: int, update: RowUpdate, user = Depends(get_current_user), db: Session = Depends(get_db)):
    row = db.query(SheetRow).filter(SheetRow.id == row_id).first()
    if row.version != update.version:
        raise HTTPException(status_code=409, detail="Conflict detected")
    row.data = update.data
    row.version += 1
    row.updated_by = user.id
    row.updated_at = datetime.utcnow()
    db.commit()
    return row
