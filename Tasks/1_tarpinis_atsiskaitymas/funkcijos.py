from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create_db import Projektas
from tkinter import *
import logging

########### Logger (Failas + Console)  ###########

logger = logging.getLogger(__name__)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] - %(message)s')
file_handler = logging.FileHandler('history_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()  
stream_handler.setFormatter(formatter) 
logger.addHandler(stream_handler)


########## SQL Connect #########

engine = create_engine('sqlite:///pilotai.db')  
Session = sessionmaker(bind=engine)
session = Session()

############### Main class Pilotas ###############

class Pilotas:
    def __init__(self, vardas, pavarde, automobilis, galia, lyga):
        
        self.vardas = vardas
        self.pavarde = pavarde
        self.automobilis = automobilis
        self.galia = galia
        self.lyga = lyga
    
    def __str__(self):
        return f"Piloto vardas, pavardė: {self.vardas} , {self.pavarde}. Automobilis: {self.automobilis}, kurio galia : {self.galia} hp. Pilotas dalyvauja {self.lyga} lygoje."   


################### Ivesti pilota ########################### 

class Add_pilot(Pilotas):
    def __init__(self, vardas, pavarde, automobilis, galia, lyga):
        try:
            super().__init__(vardas, pavarde, automobilis, galia, lyga)
            session.add(Projektas(vardas, pavarde, automobilis, galia, lyga))
            session.commit()
            logger.info(f"Ivestas naujas pilotas {vardas} , {pavarde}")
        except:
            logger.error("Ivesti duomenys netinkami")

    def naujas_langas_ivesti_pilota():
        naujas_langas = Toplevel()
        naujas_langas.title("Naujo piloto ivedimas")
        naujas_langas.geometry("550x180")
        naujas_langas.iconbitmap(r'ikonos/ikona.ico')
        
        Label(naujas_langas, text ="Naujo piloto pridejimo lentele:").pack()
        freimas = Frame(naujas_langas)
        uzrasas1 = Label(freimas, text="Įrašykite vardą:",)
        uzrasas2 = Label(freimas, text="Įrašykite pavardę:")
        uzrasas3 = Label(freimas, text="Įrašykite automobilį:")
        uzrasas4 = Label(freimas, text="Įrašykite automobilio galią (hp):")
        uzrasas5 = Label(freimas, text="Įrašykite lygą, kurioje dalyvaus pilotas:")
        
        uzrasas1.grid(row=0, column=0)
        uzrasas2.grid(row=1, column=0)
        uzrasas3.grid(row=2, column=0)
        uzrasas4.grid(row=3, column=0)
        uzrasas5.grid(row=4, column=0)
        
        vardas_laukas = Entry(freimas)
        pavarde_laukas = Entry(freimas)
        automobilis_laukas = Entry(freimas)
        galia_laukas = Entry(freimas)
        lyga_laukas = Entry(freimas)
        
        mygtukas = Button(freimas, text="Įvesti visus duomenis")
        mygtukas_exit = Button(freimas, text= "Išeiti",command=naujas_langas.destroy)
        mygtukas.bind("<Button-1>", lambda event: Add_pilot(vardas_laukas.get(), pavarde_laukas.get(), automobilis_laukas.get(), galia_laukas.get() , lyga_laukas.get()))
        
        
        mygtukas_exit.grid(row=6,column=1)
        mygtukas.grid(row=5, column=1)
        vardas_laukas.grid(row=0, column=1)
        pavarde_laukas.grid(row=1, column=1)
        automobilis_laukas.grid(row=2, column=1)
        galia_laukas.grid(row=3, column=1)
        lyga_laukas.grid(row=4, column=1)
        freimas.pack()
        naujas_langas.mainloop()


############### Update pilota ######################

class Update_pilot(Pilotas):
    
    def __init__(self, piloto_id, vardas, pavarde, automobilis, galia, lyga):
        try:
            self.piloto_id = piloto_id
            irasas = session.query(Projektas).filter_by(id=self.piloto_id).one()
            super().__init__(vardas, pavarde, automobilis, galia, lyga)
            irasas.vardas = self.vardas
            irasas.pavarde = self.pavarde
            irasas.automobilis = self.automobilis
            irasas.galia = self.galia
            irasas.lyga = self.lyga
            session.commit()
            logger.info(f"Atnaujinti piloto , kurio ID : {piloto_id} , duomenys.")
        except:
            logger.error("Ivesti duomenys netinkami")
        
    def naujas_langas_update_pilota():
        naujas_langas = Toplevel()
        naujas_langas.title("Piloto atnauijinimo lentele")
        naujas_langas.geometry("1200x300")
        naujas_langas.iconbitmap(r'ikonos/ikona.ico')
        
        Label(naujas_langas, text ="Visi uzsiregistrave pilotai:").pack()
        freimas = Frame(naujas_langas)
        uzrasas1 = Label(freimas, text="Įrašykite vardą:",)
        uzrasas2 = Label(freimas, text="Įrašykite pavardę:")
        uzrasas3 = Label(freimas, text="Įrašykite automobilį:")
        uzrasas4 = Label(freimas, text="Įrašykite automobilio galią (hp):")
        uzrasas5 = Label(freimas, text="Įrašykite lygą, kurioje dalyvaus pilotas:")
        uzrasas6 = Label(freimas, text="Įrašykite piloto, kurio duomenis norite pakeisti ID:")
        
        scrollbaras = Scrollbar(naujas_langas) 
        saraso_deze = Listbox(naujas_langas, width= 100 , height= 75, yscrollcommand=scrollbaras.set) 
        scrollbaras.config(command=saraso_deze.yview) 
        saraso_deze.insert(0, *session.query(Projektas).all()) 
        
        scrollbaras.pack(side=RIGHT, fill=Y)
        saraso_deze.pack(side=RIGHT)
        
        uzrasas1.grid(row=1, column=0)
        uzrasas2.grid(row=2, column=0)
        uzrasas3.grid(row=3, column=0)
        uzrasas4.grid(row=4, column=0)
        uzrasas5.grid(row=5, column=0)
        uzrasas6.grid(row=0, column=0)
        
        update_vardas = Entry(freimas)
        vardas_laukas = Entry(freimas)
        pavarde_laukas = Entry(freimas)
        automobilis_laukas = Entry(freimas)
        galia_laukas = Entry(freimas)
        lyga_laukas = Entry(freimas)
        
        mygtukas = Button(freimas, text="Atnaujinti duomenis")
        mygtukas_exit = Button(freimas, text= "Išeiti",command=naujas_langas.destroy)
        mygtukas.bind("<Button-1>", lambda event: Update_pilot(update_vardas.get(), vardas_laukas.get(), pavarde_laukas.get(), automobilis_laukas.get(), galia_laukas.get() ,lyga_laukas.get()))
        
        mygtukas_exit.grid(row=7,column=1)
        mygtukas.grid(row=6, column=1)
        update_vardas.grid(row=0,column=1)
        vardas_laukas.grid(row=1, column=1)
        pavarde_laukas.grid(row=2, column=1)
        automobilis_laukas.grid(row=3, column=1)
        galia_laukas.grid(row=4, column=1)
        lyga_laukas.grid(row=5, column=1)
        freimas.pack()
        naujas_langas.mainloop()


################ Visi pilotai (paziureti visus) ##############

class View_all:

    def naujas_langas_visi_pilotai():
        naujas_langas = Toplevel()
        naujas_langas.title("Pilotai")
        naujas_langas.geometry("1000x300")
        naujas_langas.iconbitmap(r'ikonos/ikona.ico')
        freimas_apacia = Frame(naujas_langas)
        freimas_virsus = Frame(naujas_langas)
        uzrasas1 = Label(freimas_virsus, text= "Visi pilotai :")
        scrollbaras = Scrollbar(naujas_langas) 
        
        saraso_deze = Listbox(naujas_langas, width= 110 , height= 55, yscrollcommand=scrollbaras.set) 
        scrollbaras.config(command=saraso_deze.yview) 
        
        saraso_deze.insert(0, *session.query(Projektas).all()) 
        uzrasas1.grid(row=0, column=0)
        mygtukas = Button(freimas_apacia, text="Eiti atgal",command=naujas_langas.destroy)
        mygtukas.grid(row=2, column=0)
        scrollbaras.pack(side=RIGHT, fill=Y)
        saraso_deze.pack(side=RIGHT)
        freimas_apacia.pack(side=BOTTOM)
        freimas_virsus.pack(side=TOP)
        naujas_langas.mainloop()
        
############# Pilotu paieska pagal kriterijus ###########

class Search_by:

    def __init__(self, vardas, pavarde, automobilis, galia_nuo, galia_iki, lyga, saraso_laukas):
        saraso_laukas.delete(0, END)
        objektai = session.query(Projektas) 
        self.vardas = vardas
        self.pavarde = pavarde
        self.automobilis = automobilis
        self.galia_nuo = galia_nuo
        self.galia_iki = galia_iki
        self.lyga = lyga
        if len(vardas) > 0:
            objektai = objektai.filter(Projektas.vardas == self.vardas)
        if len(pavarde) > 0:
            objektai = objektai.filter(Projektas.pavarde == self.pavarde)
        if len(automobilis) > 0:
            objektai = objektai.filter(Projektas.automobilis.ilike(f"%{self.automobilis}") == self.automobilis)
        if len(galia_nuo) > 0:
            objektai = objektai.filter(Projektas.galia >= self.galia_nuo)
        if len(galia_iki) > 0:
            objektai = objektai.filter(Projektas.galia <= self.galia_iki)
        if len(lyga) > 0:
            objektai = objektai.filter(Projektas.lyga == self.lyga) 
        
        objektai = objektai.all()
        saraso_laukas.insert(0, *objektai)
        
    def naujas_langas_paieska_pagal_kriterijus():
        naujas_langas = Toplevel()
        freimas = Frame(naujas_langas)
        freimas_apacia = Frame(naujas_langas)
        naujas_langas.iconbitmap(r'ikonos/ikona.ico')
        naujas_langas.geometry("750x400")  
        naujas_langas.title("Paieska pagal kriterijus")
        
        uzrasas1 = Label(freimas, text= "vardas:")
        uzrasas2 = Label(freimas, text= "pavarde:")
        uzrasas3 = Label(freimas, text= "automobilis:")
        uzrasas4 = Label(freimas, text= "galia nuo:")
        uzrasas5 = Label(freimas, text= "galia iki:")
        uzrasas6 = Label(freimas, text= "lyga:")
        
        uzrasas1.grid(row=0, column=4)
        uzrasas2.grid(row=2, column=4)
        uzrasas3.grid(row=4, column=4)
        uzrasas4.grid(row=6, column=4)
        uzrasas5.grid(row=8, column=4)
        uzrasas6.grid(row=10, column=4)
        
        laukas1 = Entry(freimas)
        laukas2 = Entry(freimas)
        laukas3 = Entry(freimas)
        laukas4 = Entry(freimas)
        laukas5 = Entry(freimas)
        laukas6 = Entry(freimas)

        mygtukas_exit = Button(freimas_apacia, text= "Išeiti", command=naujas_langas.destroy) 
        mygtukas_ieskoti = Button(freimas, text="Ieskoti")
        mygtukas_ieskoti.bind("<Button-1>",lambda event: Search_by(laukas1.get(), laukas2.get(), laukas3.get(), laukas4.get(), laukas5.get(), laukas6.get(), saraso_laukas))
        saraso_laukas = Listbox(naujas_langas, width=100, height=35)

        laukas1.grid(row=1, column=4)
        laukas2.grid(row=3, column=4)
        laukas3.grid(row=5, column=4)
        laukas4.grid(row=7, column=4)
        laukas5.grid(row=9, column=4)
        laukas6.grid(row=11, column=4)
        mygtukas_ieskoti.grid(row=12, column=4)
        mygtukas_exit.grid(row=0,column=0)
        
        saraso_laukas.pack(side=RIGHT)
        freimas_apacia.pack(side=BOTTOM)
        freimas.pack(side = LEFT)
        naujas_langas.mainloop()


########## Delete ###########

class Delete:
    
    def __init__(self, record_id):
        try:
            self.record_id = record_id
            irasas = session.query(Projektas).get(self.record_id)
            session.delete(irasas)
            session.commit()
            logger.info(f"Istrintas pilotas kurio ID -  {self.record_id}.")
        except:
            logger.error("Pasirinkto ID nera")

    def naujas_langas_istrinti_pilota():
        naujas_langas = Toplevel()
        freimas = Frame(naujas_langas)
        naujas_langas.geometry("1200x400") 
        naujas_langas.iconbitmap(r'ikonos/ikona.ico')
        
        Label(naujas_langas, text ="Piloto ištrinimo lentelė:").pack()
        uzrasas1 = Label(freimas, text="Įrašykite piloto ID, kurį norite ištrinti: ",)
        uzrasas1.grid(row=0, column=0)
        istrinimo_id = Entry(freimas)
        
        scrollbaras = Scrollbar(naujas_langas) 
        saraso_deze = Listbox(naujas_langas, width= 120 , height= 35, yscrollcommand=scrollbaras.set) 
        scrollbaras.config(command=saraso_deze.yview) 
        saraso_deze.insert(0, *session.query(Projektas).all()) 
        
        scrollbaras.pack(side=RIGHT, fill=Y)
        saraso_deze.pack(side=RIGHT)
        
        mygtukas = Button(freimas, text="Ištrinti pilotą")
        mygtukas_exit = Button(freimas, text= "Išeiti", command=naujas_langas.destroy)
        mygtukas.bind("<Button-1>", lambda event: Delete(istrinimo_id.get()))
        
        istrinimo_id.grid(row=0,column=1)
        mygtukas_exit.grid(row=1,column=0)
        mygtukas.grid(row=1, column=1)
        freimas.pack(side=LEFT)
        naujas_langas.mainloop()