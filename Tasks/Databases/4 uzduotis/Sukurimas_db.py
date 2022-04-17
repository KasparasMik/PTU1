from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Uzduotis_4.db')  
Base = declarative_base()

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column("vardas", String)
    l_name = Column("pavarde", String)
    email = Column("email", String)   # pakeist i date , be laiko bus (su datetime bus su laiku ir mikrosekundemis)

    def __init__(self, id, f_name, l_name, email):
        self.id = id
        self.f_name = f_name
        self.l_name = l_name
        self.email = email

    def __repr__(self):
        return f"{self.id}: {self.f_name} {self.l_name}, {self.mail}."


class

Base.metadata.create_all(engine)
