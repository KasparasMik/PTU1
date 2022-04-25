from tkinter import *

langas = Tk()
virsus_frame = Frame(langas)
apacia_frame = Frame(langas)




class Irasas():   # Tevine klase, kuri paima tik suma (is esmes cia funkcija funkcijoj, kuri tik paima)
    def __init__(self, suma):
        self.suma = suma
    # Getter / Setter   
    # @property   # Getteris (Dekoratorius vadinasi)
    # def setter_suma(self):
    #     return self.__suma
    #                                   
    # @setter_suma.setter  # Setteris 
    # def setter_suma(self, naujas):
    #     if naujas < 0:
    #         print("Suma negali buti minusine! Iveskite skaiciu be minuso ženklo. ")
    #     else:
    #         self.__suma = naujas


class Pajamu_irasas(Irasas):   # paveldim tevine klase, del iraso. Nes ji ima apskritai bet koki irasa
    def __init__(self, suma, siuntejas, papildoma_info):  # Visada turi buti __init__ klaseje, tada viskas buna all good.
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

    def __str__(self):
        return f"Pajamu irasas yra: {self.suma}, {self.siuntejas}, {self.papildoma_info}"
    

class Islaidu_irasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga

    def __str__(self):
        return f"Islaidu irasas yra: {self.suma}, {self.atsiskaitymo_budas}, {self.isigyta_preke_paslauga}"
    

class Biudzetas():
    def __init__(self):  
        self.zurnalas = []
        # str representing object name in string
    def __str__(self):
        return f"Zurnalas yra: {self.zurnalas}"

    def ivesti_pajamas(self, suma, siuntejas, papildoma_informacija):  # funkcija ivesti pajamas, paimant kita klase
        pajamu_irasas_1 = Pajamu_irasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamu_irasas_1)  # i zurnala musu klaseje apendina irasus
        

    def ivesti_islaidas(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidu_irasas_1 = Islaidu_irasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidu_irasas_1)  # i zurnala musu klaseje apendina irasus

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, Pajamu_irasas): 
                balansas += irasas.suma  # is visu nurodytu ir papildytu zurnale reiksmiu, paima butent suma ir ja prideda. 
            if isinstance(irasas, Islaidu_irasas):
                balansas -= irasas.suma # Rasyt galima su pliusu, kadangi nurodem kad atimt, tai atima automatiskai, nes pildom per islaidu irasa
        return balansas

    def gauti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, Pajamu_irasas): # jei yra irasas - pajamu iraso klasej, tada spausdinam (nu ar toks buvo ) tikrina
                print(f"Pajamos: {irasas.suma} BTC. Siuntejas:  {irasas.siuntejas}. Papildoma informacija:  {irasas.papildoma_info}.")
            if isinstance(irasas, Islaidu_irasas):
                print(f"Išlaidos: {irasas.suma} BTC. Atsiskaitymo budas: {irasas.atsiskaitymo_budas}. Isigyta paslauga/preke:  {irasas.isigyta_preke_paslauga}.")
        


mano_biudzetas = Biudzetas()
################ GUI (2) ########################## 

def uzdaryti(langas):
    langas.destroy()


# def pajamu_ivestis():
#     suma = suma_langas.get()
#     siuntejas = siuntejas_langas.get()
#     papildoma_info = papildoma_info_langas.get()
#     mano_biudzetas.ivesti_pajamas(suma,siuntejas,papildoma_info)
    
def naujas_langas_pajamos():
    
    naujas_langas = Toplevel()
    naujas_langas.title("Pajamu pildymo lentele")
    naujas_langas.geometry("450x120")
    Label(naujas_langas,
        text ="Pajamu ivesties lentele:").pack()
    freimas = Frame(naujas_langas)
    
    uzrasas1 = Label(freimas, text="Įrašykite sumą",)
    uzrasas2 = Label(freimas, text="Įrašykite siunteja")
    uzrasas3 = Label(freimas, text="Įrašykite papildoma info")
    
    uzrasas1.grid(row=0, column=0)
    uzrasas2.grid(row=1, column=0)
    uzrasas3.grid(row=2, column=0)
    
    
    suma_langas = Entry(freimas)
    siuntejas_langas = Entry(freimas)
    papildoma_info_langas = Entry(freimas)

    # mygtukas = Button(freimas, text="Įvesti visus duomenis", command=mano_biudzetas.ivesti_pajamas(suma_langas,siuntejas_langas,papildoma_info_langas))
    mygtukas = Button(freimas, text="Įvesti visus duomenis", command= mano_biudzetas.ivesti_pajamas(suma_langas.get(),siuntejas_langas.get(),papildoma_info_langas.get()))
    

    mygtukas.grid(row=4, column=1)
    suma_langas.grid(row=0, column=1)
    siuntejas_langas.grid(row=1, column=1)
    papildoma_info_langas.grid(row=2, column=1)
    freimas.pack()
    naujas_langas.mainloop()





def naujas_langas_islaidos():
    naujas_langas = Toplevel()
    naujas_langas.title("Islaidu pildymo lentele")
    naujas_langas.geometry("450x120")
    Label(naujas_langas,
        text ="Islaidu ivesties lentele:").pack()
    freimas = Frame(naujas_langas)
    uzrasas1 = Label(freimas, text="Įrašykite sumą")
    uzrasas2 = Label(freimas, text="Įrašykite atsiskaitymo buda")
    uzrasas3 = Label(freimas, text="Įrašykite isigyta preke/paslauga")
    uzrasas1.grid(row=0, column=0)
    uzrasas2.grid(row=1, column=0)
    uzrasas3.grid(row=2, column=0)
    suma = Entry(naujas_langas)
    atsiskaitymo_budas = Entry(freimas)
    isigyta_preke_paslauga = Entry(freimas)
    
    mygtukas = Button(freimas, text="Įvesti visus duomenis", command=mano_biudzetas.ivesti_islaidas(suma.get(suma),atsiskaitymo_budas.get(atsiskaitymo_budas),isigyta_preke_paslauga.get(isigyta_preke_paslauga)))
    mygtukas.grid(row=4, column=1)
    

    
    suma.grid(row=0, column=1)
    atsiskaitymo_budas.grid(row=1, column=1)
    isigyta_preke_paslauga.grid(row=2, column=1)
    freimas.pack()
    naujas_langas.mainloop()


def naujas_langas_balansas():
    naujas_langas = Toplevel()
    naujas_langas.title("Balansas")
    naujas_langas.geometry("220x70")
    freimas = Frame(naujas_langas)
    uzrasas1 = Label(freimas, text=f"Balansas yra : ")
    balansas_uzrasas = Label(freimas, text=mano_biudzetas.gauti_balansa()) 
    balansas_uzrasas.grid(row=0, column=2)
    uzrasas1.grid(row=0, column=0)
    mygtukas = Button(freimas, text="Eiti atgal")
    mygtukas.grid(row=3, column=2)
    freimas.pack()
    naujas_langas.mainloop()


def naujas_langas_ataskaita():
    naujas_langas = Toplevel()
    naujas_langas.title("Ataskaita")
    naujas_langas.geometry("420x100")
    freimas = Frame(naujas_langas)
    uzrasas1 = Label(freimas, text="Ataskaita yra : ")
    scrollbaras = Scrollbar(naujas_langas) # Scroll baras
    sarasas = mano_biudzetas.gauti_ataskaita()  
    saraso_deze = Listbox(naujas_langas, width= 45 , height= 25, yscrollcommand=scrollbaras.set,text=sarasas) # sulinkina scroll bara su langu
    scrollbaras.config(command=saraso_deze.yview)  # o cia kai scrolinsim
    
    saraso_deze.insert(END, sarasas) 
    uzrasas1.grid(row=0, column=0)
    mygtukas = Button(freimas, text="Eiti atgal")
    mygtukas.grid(row=2, column=0)
    scrollbaras.pack(side=RIGHT, fill=Y)
    saraso_deze.pack(side=RIGHT)
    freimas.pack()
    naujas_langas.mainloop()


langas.geometry("450x100")
langas.title("Mini biudzetas")

mygtukas_pajamos = Button(virsus_frame, text="Nurodyti pajamas",command=naujas_langas_pajamos)
mygtukas_islaidos = Button(virsus_frame, text="Nurodyti islaidas",command=naujas_langas_islaidos)
mygtukas_balansas = Button(virsus_frame, text="Pamatyti balansa",command=naujas_langas_balansas)
mygtukas_ataskaita = Button(virsus_frame, text="Pateikti ataskaita",command=naujas_langas_ataskaita)

# mygtukas_pajamos.bind("<Button-1>")
# langas.bind("<Return>")

virsus_frame.pack()
apacia_frame.pack()

mygtukas_pajamos.grid(row=0, column=0)
mygtukas_islaidos.grid(row=0, column=1)
mygtukas_balansas.grid(row=0, column=2)
mygtukas_ataskaita.grid(row=0, column=3)

langas.mainloop()

print(mano_biudzetas.zurnalas[0])




















######## 1 Bandymas #########


# class GUI_main:
#     def __init__(self, langas=Tk()):
#         # main langas
#         self.langas = langas
#         self.langas.title("Biudzetas")
#         self.langas.geometry("250x200")
#         self.langas.configure(bg='lightgreen')
        
#         self.frame = Frame(self.langas)
        
#         #Mygtukai
#         self.button_pajamos = Button(self.frame, text="Ivesti pajamas",width=5, background="green", command=self.naujas_langas_pajamos)
#         self.button_pajamos.pack(side=TOP)
        
#         self.button_islaidos = Button(self.frame, text="Ivesti islaidas",width=5, background="red", command=self.naujas_langas_islaidos)
#         self.button_islaidos.pack(side=TOP)
        
#         self.button_balansas = Button(self.frame, text="Ivesti islaidas",width=5, background="gray", command=self.naujas_langas_balansas)
#         self.button_balansas.pack(side=TOP)
        
#         self.button_ataskaita = Button(self.frame, text="Ivesti islaidas",width=5, background="yellow", command=self.naujas_langas_ataskaita)
#         self.button_ataskaita.pack(side=TOP)
        
#         self.frame.pack() 
        
#     def naujas_langas_pajamos(self):
#         self.naujas = Toplevel(self.langas)
#         self.app = Pajamu_irasas(self.naujas)
    
#     def naujas_langas_islaidos(self):
#         self.naujas = Toplevel(self.langas)
#         self.app = Islaidu_irasas(self.naujas)
    
#     def naujas_langas_balansas(self):
#         self.naujas = Toplevel(self.langas)
#         self.app = Biudzetas.gauti_balansa(self.naujas)
    
#     def naujas_langas_ataskaita(self):
#         self.naujas = Toplevel(self.langas)
#         self.app = Biudzetas.gauti_ataskaita(self.naujas)
    
#     def uzdaryti(self):
#         self.langas.destroy()




################ Biudzetas meniu ciklas pradzia ############################

# mano_biudzetas = Biudzetas()

# while True:
#     print("Pasirinkite veiksmą: ")
#     print("1 - Įvesti pajamas")
#     print("2 - Įvesti išlaidas")
#     print("3 - Gauti balansą")
#     print("4 - Gauti ataskaitą")
#     print("0 - Išeiti iš programos")
#     pasirinkimas = input()
#     if pasirinkimas:
#         if pasirinkimas == "1":
#             print("Įveskite pajamas: ")
#             suma = int(input("Suma(BTC): "))
#             siuntejas = input("Siuntėjas: ")
#             papildoma_informacija = input("Papildoma informacija: ")
#             mano_biudzetas.ivesti_pajamas(suma, siuntejas, papildoma_informacija) # iveda visas reiksmes kurias ivede useris 
#             print("Pajamos įvestos sėkmingai!")
#         elif pasirinkimas == "2":
#             print("Įveskite išlaidas: ")
#             suma= int(input("Suma(BTC): "))
#             isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
#             atsiskaitymo_budas = input("Atsiskaitymo būdas: ")
#             mano_biudzetas.ivesti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
#             print("Išlaidos sėkmingai įvestos!")
#         elif pasirinkimas == "3":
#             print(f"Sąskaitos balansas: {mano_biudzetas.gauti_balansa()} BTC.")
#         elif pasirinkimas == "4":
#             mano_biudzetas.gauti_ataskaita()
#         elif pasirinkimas == "0":
#             break


