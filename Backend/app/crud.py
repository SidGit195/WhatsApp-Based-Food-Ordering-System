from sqlalchemy.orm import Session
from app import models, schemas
from app.twilio_client import twilio_client

# Menu
def create_menu_item(db: Session, item: schemas.MenuItemCreate):
    db_item = models.MenuItem(**item.dict())
    db.add(db_item); db.commit(); db.refresh(db_item)
    return db_item

def list_menu(db: Session):
    return db.query(models.MenuItem).all()

def get_menu_item(db: Session, item_id: int):
    return db.query(models.MenuItem).filter(models.MenuItem.id==item_id).first()

# Orders
def create_order(db: Session, order_in: schemas.OrderCreate):
    items = [models.OrderItem(menu_item_id=i.menu_item_id, quantity=i.quantity)
             for i in order_in.items]
    db_order = models.Order(
        customer_name=order_in.customer_name,
        whatsapp_number=order_in.whatsapp_number,
        items=items
    )
    db.add(db_order); db.commit(); db.refresh(db_order)
    twilio_client.send_order_confirmation(db_order)
    return db_order

def list_orders(db: Session):
    return db.query(models.Order).all()

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id==order_id).first()

def update_order_status(db: Session, order_id: int, status: schemas.OrderUpdate):
    order = get_order(db, order_id)
    order.status = status.status
    db.commit(); db.refresh(order)
    twilio_client.send_status_update(order)
    return order

def cancel_order(db: Session, order_id: int):
    order = get_order(db, order_id)
    order.status = models.OrderStatus.canceled
    db.commit()
    twilio_client.send_cancellation(order)
    return order