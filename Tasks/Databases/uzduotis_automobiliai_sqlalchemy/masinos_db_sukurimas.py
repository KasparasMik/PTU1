from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///Uzduotis_4.db')  
Base = declarative_base()

class Projektas(Base):
    __tablename__ = "Automobiliai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    marke = Column("marke", String)
    modelis = Column("modelis", String)
    spalva = Column("spalva", String)   # pakeist i date , be laiko bus (su datetime bus su laiku ir mikrosekundemis)
    pagaminimo_metai = Column("pagaminimo metai", Integer)
    kaina = Column("kaina", Float)

    def __init__(self, marke, modelis , spalva, pagaminimo_metai , kaina):
        self.marke = marke
        self.modelis = modelis
        self.spalva = spalva
        self.pagaminimo_metai = pagaminimo_metai
        self.kaina = kaina

    def __repr__(self):
        return f"{self.id}. {self.marke} {self.modelis}, {self.spalva}, {self.pagaminimo_metai}, {self.kaina} EUR."
    
Base.metadata.create_all(engine)
