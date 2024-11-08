from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from api.dependencies.database import Base

# Sandwich Model
class Sandwich(Base):
    __tablename__ = 'sandwiches'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_name = Column(String(100), unique=True, nullable=False)
    price = Column(Float, nullable=False)

    recipes = relationship("Recipe", back_populates="sandwich")
    order_details = relationship("OrderDetail", back_populates="sandwich")

# Resource Model
class Resource(Base):
    __tablename__ = 'resources'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    item = Column(String(100), unique=True, nullable=False)
    amount = Column(Integer, nullable=False, server_default='0')

    recipes = relationship("Recipe", back_populates="resource")

# Recipe Model
class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sandwich_id = Column(Integer, ForeignKey('sandwiches.id'), nullable=False)
    resource_id = Column(Integer, ForeignKey('resources.id'), nullable=False)
    amount = Column(DECIMAL(precision=4, scale=2), nullable=False, server_default='0.0')

    sandwich = relationship("Sandwich", back_populates="recipes")
    resource = relationship("Resource", back_populates="recipes")

# Order Model
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    order_date = Column(DateTime, nullable=False, server_default=func.now())
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")

# OrderDetail Model
class OrderDetail(Base):
    __tablename__ = 'order_details'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    sandwich_id = Column(Integer, ForeignKey('sandwiches.id'), nullable=False)
    amount = Column(Integer, nullable=False)

    sandwich = relationship("Sandwich", back_populates="order_details")
    order = relationship("Order", back_populates="order_details")
