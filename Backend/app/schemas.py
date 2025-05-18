from pydantic import BaseModel, conint
from typing import List
from app.models import OrderStatus

class MenuItemBase(BaseModel):
    name: str
    description: str = None
    price: float
    available: bool = True

class MenuItemCreate(MenuItemBase): pass
class MenuItem(MenuItemBase):
    id: int
    class Config: from_attributes = True

class OrderItemCreate(BaseModel):
    menu_item_id: int
    quantity: conint(gt=0) = 1

class OrderBase(BaseModel):
    customer_name: str
    whatsapp_number: str
    items: List[OrderItemCreate]

class OrderCreate(OrderBase): pass

class OrderUpdate(BaseModel):
    status: OrderStatus

class OrderItem(OrderItemCreate):
    id: int
    class Config: from_attributes = True

class Order(OrderBase):
    id: int
    status: OrderStatus
    class Config: from_attributes = True