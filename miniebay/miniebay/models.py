from sqlalchemy import Column, DateTime, Integer, Float, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from flask_jsontools import JsonSerializableBase
from sqlalchemy import inspect
import datetime

Base = declarative_base(cls=(JsonSerializableBase,))

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(64), unique=True)
    password = Column(String(18))
    firstname = Column(String(64))
    lastname = Column(String(64))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    def to_json(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String(100))
    description = Column(String(1024))
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)

    def to_json(self):
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }
