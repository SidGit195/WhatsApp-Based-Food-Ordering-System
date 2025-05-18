from sqlalchemy import Column, Integer, String, Float, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class OrderStatus(str, enum.Enum):
    pending = "pending"
    preparing = "preparing"
    out_for_delivery = "out-for-delivery"
    delivered = "delivered"
    canceled = "canceled"

class MenuItem(Base):
    __tablename__ = "menu_items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    available = Column(Boolean, default=True)

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"))
    quantity = Column(Integer, default=1)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    whatsapp_number = Column(String, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    items = relationship("OrderItem", cascade="all, delete-orphan")