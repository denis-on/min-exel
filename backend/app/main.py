from fastapi import FastAPI
from app.database import Base, engine
from app.routes import users, sheets, rows

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Excel API")

app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(sheets.router, prefix="/api/sheets", tags=["Sheets"])
app.include_router(rows.router, prefix="/api/rows", tags=["Rows"])
