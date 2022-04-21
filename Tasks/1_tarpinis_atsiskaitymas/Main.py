from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tkinter import *
from funkcijos import *

engine = create_engine('sqlite:///pilotai.db')  
Session = sessionmaker(bind=engine)
session = Session()

langas = Tk()
freimas = Frame(langas)
langas.iconbitmap(r'ikonos/ikona.ico')

img = PhotoImage(file = 'ikonos/LASF_updated.png')
panel = Label(langas, image = img)
panel.pack(side=BOTTOM)

langas.geometry("700x250")   
langas.title("Pilotai")

mygtukas_ivesti_nauja_pilota = Button(freimas, text="Ivesti nauja pilotą",command=Add_pilot.naujas_langas_ivesti_pilota)
mygtukas_update_pilota = Button(freimas, text="Pakeisti piloto duomenis",command=Update_pilot.naujas_langas_update_pilota)
mygtukas_perziureti_visus_pilotus = Button(freimas, text="Perziureti visus pilotus",command=View_all.naujas_langas_visi_pilotai)
mygtukas_paieska_pagal_kriterijus = Button(freimas, text="Pilotu paieska pagal kriterijus",command=Search_by.naujas_langas_paieska_pagal_kriterijus)
mygtukas_istrinti_pilota = Button(freimas, text="Istrinti pilota",command=Delete.naujas_langas_istrinti_pilota)

freimas.pack()

mygtukas_ivesti_nauja_pilota.grid(row=0, column=0)
mygtukas_update_pilota.grid(row=0, column=1)
mygtukas_perziureti_visus_pilotus.grid(row=0, column=2)
mygtukas_paieska_pagal_kriterijus.grid(row=0, column=3)
mygtukas_istrinti_pilota.grid(row=0, column=4)

langas.mainloop()