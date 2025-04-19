import os
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)

    orders = relationship("Order", back_populates="user")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "orders": [order.to_dict() for order in self.orders]
        }

class Food(Base):
    __tablename__ = "food"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    
    orders = relationship("Order", back_populates="food")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "orders": [order.to_dict() for order in self.orders]
        }

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("food.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="orders")
    food = relationship("Food", back_populates="orders")
    
    def to_dict(self):
        return {
            "id": self.id,
            "food_id": self.food_id,
            "user_id": self.user_id,
            "user": self.user.name if self.user else None,
            "food": self.food.name if self.food else None
        }