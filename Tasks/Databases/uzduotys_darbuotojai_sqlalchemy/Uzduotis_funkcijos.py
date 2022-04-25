# 1 užduotis   ( https://github.com/DonatasNoreika/python1lygis/wiki/Duomen%C5%B3-baz%C4%97s-2 )
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Uzduotis_db_sukurimas import Projektas
from tkinter import *

langas = Tk()
virsus_frame = Frame(langas)
apacia_frame = Frame(langas)

engine = create_engine('sqlite:///Uzduotis_from_github_noreika_1.db')  
Session = sessionmaker(bind=engine)
session = Session()

def irasyti_darbuotoja(name, surname, work, date_of_birth, salary):
    session.add(Projektas(name, surname, date_of_birth, work, salary))
    session.commit()

def perziureti_darbuotojus():
    return session.query(Projektas).all()
    # visi = session.query(Projektas).all()
    # [print(i) for i in visi]

def istrinti_darbuotoja(record_id):
    irasas = session.query(Projektas).get(record_id)
    session.delete(irasas)
    session.commit()

def atnaujinti_darbuotoja(iraso_vardas, name, surname, work, date_of_birth, salary):
    irasas = session.query(Projektas).filter_by(name=f"{iraso_vardas}").one()
    irasas.name = name
    irasas.surname = surname
    irasas.work = work
    irasas.date_of_birth = date_of_birth
    irasas.salary = salary
    session.commit()

##################################### GUI ##############################################

# def quit():
#     Toplevel.destroy()

###################################  ADD    ##########################################

def spausdinti_paimti_reiksme_darbuotojui(name,surname,work,date_of_birth,salary):
    ivesta1 = name.get()
    ivesta2 = surname.get()
    ivesta3 = work.get()
    ivesta4 = date_of_birth.get()
    ivesta5 = salary.get()
    irasyti_darbuotoja(ivesta1, ivesta2, ivesta3, ivesta4, ivesta5) 

def naujas_langas_ivesti_darbuotoja():
    naujas_langas = Toplevel()
    naujas_langas.title("Darbuotojai")
    naujas_langas.geometry("550x180")
    
    Label(naujas_langas, text ="Naujo darbuotojo pridejimo lentele:").pack()
    freimas = Frame(naujas_langas)
    uzrasas1 = Label(freimas, text="Įrašykite vardą",)
    uzrasas2 = Label(freimas, text="Įrašykite pavardę")
    uzrasas3 = Label(freimas, text="Įrašykite darba")
    uzrasas4 = Label(freimas, text="Įrašykite gimimo data")
    uzrasas5 = Label(freimas, text="Įrašykite valandini atlyginima")
    
    uzrasas1.grid(row=0, column=0)
    uzrasas2.grid(row=1, column=0)
    uzrasas3.grid(row=2, column=0)
    uzrasas4.grid(row=3, column=0)
    uzrasas5.grid(row=4, column=0)
    
    name_laukas = Entry(freimas)
    surname_laukas = Entry(freimas)
    work_laukas = Entry(freimas)
    date_of_birth_laukas = Entry(freimas)
    salary_laukas = Entry(freimas)
    
    mygtukas = Button(freimas, text="Įvesti visus duomenis")
    mygtukas_exit = Button(freimas, text= "Išeiti",command=naujas_langas.destroy)
    mygtukas.bind("<Button-1>", lambda event: spausdinti_paimti_reiksme_darbuotojui(name_laukas, surname_laukas, work_laukas, date_of_birth_laukas , salary_laukas))
    
    mygtukas_exit.grid(row=6,column=1)
    mygtukas.grid(row=5, column=1)
    name_laukas.grid(row=0, column=1)
    surname_laukas.grid(row=1, column=1)
    work_laukas.grid(row=2, column=1)
    date_of_birth_laukas.grid(row=3, column=1)
    salary_laukas.grid(row=4, column=1)
    freimas.pack()
    naujas_langas.mainloop()

################################################# UPDATE  ###############################################################################################

def paimti_reiksme_update_darbuotojui(iraso_vardas, name,surname,work,date_of_birth,salary):
    ivesta6 = iraso_vardas.get()
    ivesta1 = name.get()
    ivesta2 = surname.get()
    ivesta3 = work.get()
    ivesta4 = date_of_birth.get()
    ivesta5 = salary.get()
    atnaujinti_darbuotoja(ivesta6, ivesta1, ivesta2, ivesta3, ivesta4, ivesta5) 

def naujas_langas_keisti_darbuotoja():
    naujas_langas = Toplevel()
    freimas = Frame(naujas_langas)
    Label(naujas_langas, text ="Darbuotojo update lentele:").pack()
    
    uzrasas6 = Label(freimas, text="Iveskite darbuotojo kurio duomenis norite keisti, pilną vardą: ")
    uzrasas1 = Label(freimas, text="Įrašykite vardą",)
    uzrasas2 = Label(freimas, text="Įrašykite pavardę")
    uzrasas3 = Label(freimas, text="Įrašykite darba")
    uzrasas4 = Label(freimas, text="Įrašykite gimimo data")
    uzrasas5 = Label(freimas, text="Įrašykite valandini atlyginima")
    
    uzrasas1.grid(row=1, column=0)
    uzrasas2.grid(row=2, column=0)
    uzrasas3.grid(row=3, column=0)
    uzrasas4.grid(row=4, column=0)
    uzrasas5.grid(row=5, column=0)
    uzrasas6.grid(row=0, column=0)
    
    update_vardas = Entry(freimas)
    name_laukas = Entry(freimas)
    surname_laukas = Entry(freimas)
    work_laukas = Entry(freimas)
    date_of_birth_laukas = Entry(freimas)
    salary_laukas = Entry(freimas)
    
    mygtukas = Button(freimas, text="Atnaujinti duomenis")
    mygtukas_exit = Button(freimas, text= "Išeiti", command=naujas_langas.destroy)
    mygtukas.bind("<Button-1>", lambda event: paimti_reiksme_update_darbuotojui(update_vardas,name_laukas, surname_laukas, work_laukas, date_of_birth_laukas , salary_laukas)) # pakeist reiks
    
    mygtukas_exit.grid(row=7,column=1)
    mygtukas.grid(row=6, column=1)
    update_vardas.grid(row=0,column=1)
    name_laukas.grid(row=1, column=1)
    surname_laukas.grid(row=2, column=1)
    work_laukas.grid(row=3, column=1)
    date_of_birth_laukas.grid(row=4, column=1)
    salary_laukas.grid(row=5, column=1)
    freimas.pack()
    naujas_langas.mainloop()

############################################  DELETE   ###################################################
#Padaryt visa sarasa ju veliau, kad butu galima pazymet kuri nori istrinti (Arba nauja mygtuka, kuris leistu pasirinkti is saraso.)

def istrinti_darbuotoja_gui(name):
    ivesta1 = name.get()
    istrinti_darbuotoja(ivesta1) 

def naujas_langas_istrinti_darbuotoja():
    naujas_langas = Toplevel()
    freimas = Frame(naujas_langas)
    Label(naujas_langas, text ="Darbuotojo ištrinimo lentelė:").pack()
    uzrasas1 = Label(freimas, text="Įrašykite darbuotojo ID, kurį norite ištrinti: ",)
    
    uzrasas1.grid(row=0, column=0)
    
    istrinimo_vardas = Entry(freimas)
    
    mygtukas = Button(freimas, text="Ištrinti darbuotoja")
    mygtukas_exit = Button(freimas, text= "Išeiti", command=naujas_langas.destroy)
    mygtukas.bind("<Button-1>", lambda event: istrinti_darbuotoja_gui(istrinimo_vardas))
    
    istrinimo_vardas.grid(row=0,column=1)
    mygtukas_exit.grid(row=1,column=0)
    mygtukas.grid(row=1, column=1)
    freimas.pack()
    naujas_langas.mainloop()

################################################## VISI DARBUOTOJAI ##########################################

def naujas_langas_visi_darbuotojai():
    naujas_langas = Toplevel()
    naujas_langas.title("Darbuotojai")
    naujas_langas.geometry("420x100")
    freimas = Frame(naujas_langas)
    uzrasas1 = Label(freimas, text= "Visi darbuotojai :")
    scrollbaras = Scrollbar(naujas_langas) # Scroll baras
    
    saraso_deze = Listbox(naujas_langas, width= 45 , height= 35, yscrollcommand=scrollbaras.set) # sulinkina scroll bara su langu
    scrollbaras.config(command=saraso_deze.yview)  # o cia kai scrolinsim
    
    saraso_deze.insert(0, *perziureti_darbuotojus()) 
    uzrasas1.grid(row=0, column=0)
    mygtukas = Button(freimas, text="Eiti atgal",command=naujas_langas.destroy)
    mygtukas.grid(row=2, column=0)
    scrollbaras.pack(side=RIGHT, fill=Y)
    saraso_deze.pack(side=RIGHT)
    freimas.pack()
    naujas_langas.mainloop()

################################## MAIN ############################################



langas.geometry("600x50")  # suskaiciuot kiek tiksliai su visais langeliais  , arba pridet xujniu veliau
langas.title("Darbuotojai")

mygtukas_pajamos = Button(virsus_frame, text="Ivesti nauja darbuotoja",command=naujas_langas_ivesti_darbuotoja)
mygtukas_islaidos = Button(virsus_frame, text="Pakeisti Darbuotojo duomenis",command=naujas_langas_keisti_darbuotoja)
mygtukas_balansas = Button(virsus_frame, text="Istrinti darbuotoja",command=naujas_langas_istrinti_darbuotoja)
mygtukas_ataskaita = Button(virsus_frame, text="Pateikti visus darbuotojus",command=naujas_langas_visi_darbuotojai)



virsus_frame.pack()
apacia_frame.pack()

mygtukas_pajamos.grid(row=0, column=0)
mygtukas_islaidos.grid(row=0, column=1)
mygtukas_balansas.grid(row=0, column=2)
mygtukas_ataskaita.grid(row=0, column=3)

langas.mainloop()