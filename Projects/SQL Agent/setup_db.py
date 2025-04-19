import os
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
import urllib.parse

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    email = Column(Integer, unique=True, index=True)

    orders = relationship("Order", back_populates="user")
    
class Food(Base):
    __tablename__ = "food"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    
    orders = relationship("Order", back_populates="food")
    
class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    food_id = Column(Integer, ForeignKey("food.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    
    user = relationship("User", back_populates="orders")
    food = relationship("Food", back_populates="orders")
    
DATABASE_URL = "sqlite:///example.db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
    
    session = SessionLocal()
    
    users = [
        User(name="Akshay", age=26, email="akshay@gmail.com"),
        User(name="Abhi", age=20, email="Abhi@gmail.com"),
        User(name="Akhi", age=22, email="Akhi@gmail.com")
    ]
    
    session.add_all(users)
    session.commit()
    
    foods = [
        Food(name="Pizza", price=10.5),
        Food(name="Burger", price=7.9),
        Food(name="Pasta", price=8.5)
    ]
    
    session.add_all(foods)
    session.commit()
    
    orders = [
        Order(food_id=1, user_id=1),
        Order(food_id=2, user_id=2),
        Order(food_id=3, user_id=2)
    ]
    
    session.add_all(orders)
    session.commit()
    
    session.close()
    print("Database initialized and sample data added.")
    
if __name__ == "__main__":
    if not os.path.exists("example.db"):
        init_db()
    else:
        print("Database already exists. No changes made.")