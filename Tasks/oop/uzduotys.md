## 1 užduotis:

Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:

-   Gražina tekstą atbulai
-   Gražina tekstą mažosiomis raidėmis
-   Gražina tekstą didžiosiomis raidėmis
-   Gražina žodį pagal nurodytą eilės numerį
-   Gražina, kiek tekste yra nurodytų simbolių arba žodžių
-   Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
-   Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

Susikurti kelis klasės objektus ir išbandyti visus metodus

## 2 užduotis:

Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:

-   Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
-   Gražina, ar nurodytos sukakties metai buvo keliamieji
-   Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
-   Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą


## 3 užduotis:

-   Perdaryti 1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas, veiksmai turi būti atliekami su „Zen of Python“ tekstu
-   Perdaryti 2 užduotį taip, kad jei kuriant objektą, nepaduodamas jokia data, veiksmai turi būti atliekami su programuotojo gimtadieniu


## 4 užduotis:

-   Perdaryti 1 užduotį taip, kad spausdinant sakinio objektą, spausdintų ne objekto adresą, o įvestą tekstą
-   Perdaryti 2 užduotį taip, kad spausdinant datos objektą, spausdintų ne objekto adresą, o įvestą datą


## 5 užduotis:

Padaryti minibiudžeto programą, kuri:

-   Leistų vartotojui įvesti pajamas
-   Leistų vartotojui įvesti išlaidas
-   Leistų vartotojui parodyti pajamų/išlaidų balansą
-   Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
-   Leistų vartotojui išeiti iš programos

---


## Rekomendacija, kaip galima būtų padaryti:

-   Programa turi turėti klasę _Irasas_, kuri turėtų argumentus _tipas_ (_Pajamos_ arba _Išlaidos_) ir _suma_. Galima prirašyti **str** metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
-   Programa turi turėti klasę _Biudzetas_, kurioje būtų:

1.  Metodas **init**, kuriame sukurtas tuščias sąrašas _zurnalas_, į kurį bus dedami sukurti pajamų ir išlaidų objektai
2.  Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
3.  Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
4.  Metodas gauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
5.  Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).
