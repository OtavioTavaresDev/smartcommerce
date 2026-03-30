from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, JSON, ForeignKey
from datetime import datetime
from database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    old_price = Column(Float)
    rating = Column(Float)
    free_shipping = Column(Boolean)
    category = Column(String)
    image = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    username = Column(String)
    order_date = Column(DateTime, default=datetime.utcnow)
    items = Column(JSON)          # lista de itens do carrinho
    total = Column(Float)
    payment_method = Column(String)
    customer_data = Column(JSON)  # dados do cliente (nome, cpf, etc.)
    status = Column(String, default="completed")