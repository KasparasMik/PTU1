from sqlalchemy import Column, Integer, String, DateTime ,create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///pilotai.db')  
Base = declarative_base()

class Projektas(Base):
    __tablename__ = "Dalyviai"
    id = Column(Integer, primary_key=True, autoincrement=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    automobilis = Column("Automobilis", String) 
    galia = Column("Galia (hp)", Integer)
    lyga = Column("Lyga", String)
    uzsiregistravimo_data = Column("Uzsiregistravimo_data", DateTime, default=datetime.utcnow)
    

    def __init__(self, vardas, pavarde , automobilis, galia , lyga):
        self.vardas = vardas
        self.pavarde = pavarde
        self.automobilis = automobilis
        self.galia = galia
        self.lyga = lyga

    def __repr__(self):
        return f"Piloto ID: [{self.id}] {self.vardas} {self.pavarde}. Automobilis : {self.automobilis}, galia - {self.galia} HP. Dalyvauja {self.lyga} lygoje."
    
    def __eq__(self, other):
        return isinstance(other, Projektas) and other.id == self.id
    
Base.metadata.create_all(engine)

