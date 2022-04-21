from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from masinos_db_sukurimas import Projektas
from tkinter import *

langas = Tk()
frame = Frame(langas)

engine = create_engine('sqlite:///Uzduotis_3.db')  
Session = sessionmaker(bind=engine)
session = Session()



def search(marke, modelis, spalva, pagaminimo_metai_nuo, pagaminimo_metai_iki, kaina_nuo, kaina_iki):
    saraso_laukas.delete(0, END)
    objektai = session.query(Projektas) 
    if len(marke) > 0:
        objektai = objektai.filter(Projektas.marke == marke)
    if len(modelis) > 0:
        objektai = objektai.filter(Projektas.modelis == modelis)
    if len(spalva) > 0:
        objektai = objektai.filter(Projektas.spalva == spalva)
    if len(pagaminimo_metai_nuo) > 0:
        objektai = objektai.filter(Projektas.pagaminimo_metai >= pagaminimo_metai_nuo)
    if len(pagaminimo_metai_iki) > 0:
        objektai = objektai.filter(Projektas.pagaminimo_metai <= pagaminimo_metai_iki)
    if len(kaina_nuo) > 0:
        objektai = objektai.filter(Projektas.kaina >= kaina_nuo)
    if len(kaina_iki) > 0:
        objektai = objektai.filter(Projektas.kaina <= kaina_iki)
    
    objektai = objektai.all()
    saraso_laukas.insert(0, *objektai)
    


########################## GUI #########################

langas.geometry("550x400")  
langas.title("Automobiliai")


uzrasas1 = Label(frame, text= "Marke:")
uzrasas2 = Label(frame, text= "Modelis:")
uzrasas3 = Label(frame, text= "Spalva:")
uzrasas4 = Label(frame, text= "Metai nuo:")
uzrasas5 = Label(frame, text= "Metai iki:")
uzrasas6 = Label(frame, text= "Kaina nuo:")
uzrasas7 = Label(frame, text= "Kaina iki:")


uzrasas1.grid(row=0, column=4)
uzrasas2.grid(row=2, column=4)
uzrasas3.grid(row=4, column=4)
uzrasas4.grid(row=6, column=4)
uzrasas5.grid(row=8, column=4)
uzrasas6.grid(row=10, column=4)
uzrasas7.grid(row=12, column=4)


laukas1 = Entry(frame)
laukas2 = Entry(frame)
laukas3 = Entry(frame)
laukas4 = Entry(frame)
laukas5 = Entry(frame)
laukas6 = Entry(frame)
laukas7 = Entry(frame)

# mygtukas_exit = Button(frame, text= "Išeiti", command=langas.destroy)

mygtukas_ieskoti = Button(frame, text="Ieskoti",width=15)
mygtukas_ieskoti.bind("<Button-1>",lambda event: search(laukas1.get(), laukas2.get(), laukas3.get(), laukas4.get(), laukas5.get(), laukas6.get(), laukas7.get()))

saraso_laukas = Listbox(langas, width=40, height=35)
# saraso_laukas.insert(0, *search())


laukas1.grid(row=1, column=4)
laukas2.grid(row=3, column=4)
laukas3.grid(row=5, column=4)
laukas4.grid(row=7, column=4)
laukas5.grid(row=9, column=4)
laukas6.grid(row=11, column=4)
laukas7.grid(row=13, column=4)

mygtukas_ieskoti.grid(row=14, columnspan=2)


saraso_laukas.pack(side=RIGHT)
frame.pack(side = LEFT)



langas.mainloop()





















############

# sarasas_rodymui = []

# def add_car( marke, modelis , spalva, pagaminimo_metai , kaina):
#     session.add(Projektas(marke, modelis , spalva, pagaminimo_metai , kaina))
#     session.commit()

# def search_by_id(record_id): # isprintina. Gali but kad reiks return be print
#     irasas = session.query(Projektas).get(record_id)
#     sarasas_rodymui.append(irasas)

# def search_by_make(ieskoma_marke):  # isprintina. Gali but kad reiks return be print
#     sarasas_rodymui.append(session.query(Projektas).filter(Projektas.marke == ieskoma_marke).all())

# def search_by_model(ieskomas_modelis):  # isprintina. Gali but kad reiks return be print
#     sarasas_rodymui.append(session.query(Projektas).filter(Projektas.modelis == ieskomas_modelis).all())

# def search_by_color(spalva):  # isprintina. Gali but kad reiks return be print
#     sarasas_rodymui.append(session.query(Projektas).filter(Projektas.spalva == spalva).all())

# def search_by_year(metai):  # isprintina. Gali but kad reiks return be print
#     sarasas_rodymui.append(session.query(Projektas).filter(Projektas.pagaminimo_metai == metai).all())

# def search_by_price_from(kaina):  # isprintina. Gali but kad reiks return be print
#     sarasas_rodymui.append(session.query(Projektas).filter(Projektas.kaina >= kaina).all())
    
# def search_by_price_to(kaina):  # isprintina. Gali but kad reiks return be print
#     sarasas_rodymui.append(session.query(Projektas).filter(Projektas.kaina <= kaina).all())







# def add_car( marke, modelis , spalva, pagaminimo_metai , kaina):
    #     session.add(Projektas(marke, modelis , spalva, pagaminimo_metai , kaina))
#     session.commit()

# def search_by_id(record_id): 
#     irasas = session.query(Projektas).get(record_id)
#     print(irasas)

# def search_by_make(ieskoma_marke): 
#     print(session.query(Projektas).filter(Projektas.marke == ieskoma_marke).all())

# def search_by_model(ieskomas_modelis):  
#     print(session.query(Projektas).filter(Projektas.modelis == ieskomas_modelis).all())

# def search_by_color(spalva):  
#     print(session.query(Projektas).filter(Projektas.spalva == spalva).all())

# def search_by_year(metai):  
#     print(session.query(Projektas).filter(Projektas.pagaminimo_metai == metai).all())

# def search_by_price_from(kaina):  
#     print(session.query(Projektas).filter(Projektas.kaina >= kaina).all())
    
# def search_by_price_to(kaina):  
#     print(session.query(Projektas).filter(Projektas.kaina <= kaina).all())



