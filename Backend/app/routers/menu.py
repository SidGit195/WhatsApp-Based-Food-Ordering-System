from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

router = APIRouter(prefix="/menu", tags=["menu"])

@router.post("/", response_model=schemas.MenuItem)
def create_menu(item: schemas.MenuItemCreate, db: Session = Depends(get_db)):
    return crud.create_menu_item(db, item)

@router.get("/", response_model=list[schemas.MenuItem])
def read_menu(db: Session = Depends(get_db)):
    return crud.list_menu(db)

@router.get("/{item_id}", response_model=schemas.MenuItem)
def read_menu_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_menu_item(db, item_id)
    if not db_item:
        raise HTTPException(404, "Item not found")
    return db_item