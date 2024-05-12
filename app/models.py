import uuid
from app import db
from sqlalchemy import Column, String


class Users(db.Model):
    __tablename__ = "users"

    id = Column(String(32), primary_key=True)
    name =  Column(String(32))
    password = Column(String(32))

    def __init__(self,name,password):
        self.id = str(uuid.uuid4().hex),
        self.name = name,
        self.password = password
    
    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }