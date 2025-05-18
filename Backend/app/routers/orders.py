from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import SessionLocal

def get_db():
    db = SessionLocal(); 
    try: yield db
    finally: db.close()

router = APIRouter(prefix="/orders", tags=["orders"])

@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@router.get("/", response_model=list[schemas.Order])
def read_orders(db: Session = Depends(get_db)):
    return crud.list_orders(db)

@router.get("/{order_id}", response_model=schemas.Order)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id)
    if not db_order: raise HTTPException(404, "Order not found")
    return db_order

@router.patch("/{order_id}", response_model=schemas.Order)
def update_order(order_id: int, status: schemas.OrderUpdate, db: Session = Depends(get_db)):
    return crud.update_order_status(db, order_id, status)

@router.delete("/{order_id}", status_code=204)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    crud.cancel_order(db, order_id)