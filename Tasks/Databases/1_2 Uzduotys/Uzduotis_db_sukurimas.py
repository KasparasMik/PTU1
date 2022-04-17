from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Uzduotis_from_github_noreika_1.db')  
Base = declarative_base()

class Projektas(Base):
    __tablename__ = "Darbuotojai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column("vardas", String)
    surname = Column("pavarde", String)
    date_of_birth = Column("gimimo_data", String)   # pakeist i date , be laiko bus (su datetime bus su laiku ir mikrosekundemis)
    work = Column("pareigos", String)
    salary = Column("Atlyginimas", Float)
    works_from = Column("dirba_nuo", DateTime, default=datetime.utcnow)

    def __init__(self, name, surname, date_of_birth, work, salary):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.work = work
        self.salary = salary

    def __repr__(self):
        return f"{self.id}. {self.name} {self.surname}, {self.date_of_birth}, {self.work}, {self.salary} EUR. {self.works_from}"
    
Base.metadata.create_all(engine)
