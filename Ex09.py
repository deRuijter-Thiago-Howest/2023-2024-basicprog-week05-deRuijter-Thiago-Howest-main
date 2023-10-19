# Maak een pythonapplicatie die voor een groep personen (studenten/docenten) een
# snelheidscontrole in de straat ‘Sint Martens Latemlaan’ simuleert.
# Stap 0: we starten met een een list met personeelsleden.
# list_personeel = ["Stijn", "Gilles", "Dieter", "Christophe", "Marie"]

# Stap 1: als simulatie wordt voor elke persoon een willekeurige snelheid tussen 10 en 70km/u
# gegeneerd. Hiervoor gebruik je de functie ‘registreer_snelheidsmeting’. Het resultaat van
# deze functie is een dictionary. De key is het personeelslid, de value de willekeurige snelheid

# Stap 2: print alle snelheden per persoon af.
# Vermeld ook de straatnaam. Gebruik hiervoor een functie ‘print_snelheden_personen’

# Stap 3: vraag aan de gebruiker de maximum toegelaten snelheid in de betrokken straat.

# Stap 4: filter de overtredingen uit de dictionary.
# Gebruik hiervoor een afzonderlijke functie ‘filter_overtredingen’.
# Geef als parameter de startdictionary en de maximum toegelaten snelheid mee.
# Wat geef deze functie terug?

# Stap 5: print de boetes uit voor de overtredingen uit.
# De boete wordt als volgt berekend: 10€ per km boven de toegelaten snelheid.
# Gebruik hiervoor opnieuw een afzonderlijke functie ‘print_boetes’

from typing import Dict, List
from random import randint

#stap1: Geef een dict terug waarvan de keys de namen zijn en de values de snelheden
def registreer_snelheidsmeting(list_personen: List[str]) -> Dict[str,int]:
    dict_resultaat = {}
    for persoon in list_personen:
        #kies een snelheid
        snelheid = randint(10,70)
        #toevoegen aan dict
        dict_resultaat[persoon] = snelheid 
    return dict_resultaat

#stap2
def print_snelheden_personen(straatnaam:str,dict_snelheden:dict[str,int]) -> None:
    print(f"Geregistreerde snelheden in de straat {straatnaam}")
    for key, value in dict_snelheden.items():
        print(f"{key:10}  \t\t  {value} km/u")



#stap4: filteren houdt in dat je een kleinere verzameling teruggeeft.
def filter_overtredingen(max_snelheid:int, dict_snelheden:Dict[str,int]) -> Dict[str,int]:
    dict_resultaat = {}
    for naam,snelheid in dict_snelheden.items():
        #is de snelheid boven de maximum snelheid
        if snelheid > max_snelheid:
            #naam en snelheid in de nieuwe dict steken
            dict_resultaat[naam] = snelheid
    return dict_resultaat


#stap5: print de boetes uit voor de overtredingen uit.
# De boete wordt als volgt berekend: 10€ per km boven de toegelaten snelheid.
# Gebruik hiervoor opnieuw een afzonderlijke functie ‘print_boetes’

# def print_boetes(dict_overtredingen:dict[str,int]) -> dict[str,int]:
#     dict_resultaat = {}
#     for naam,snelheid in dict_overtredingen.items():
#         over = snelheid - max_snelheid
#         boete = over * 10
#         dict_resultaat[naam] = boete
#     return dict_resultaat

def print_boetes(dict_overtredingen:dict[str,int]) -> dict[str,int]:
    for naam,snelheid in dict_overtredingen.items():
        boete = (snelheid - max_snelheid) * 10
        print(f"{naam:10} \t\t boete: {boete}$")


list_docenten = ["Stijn", "Marie", "Joerie", "Henk", "Dieter"]
# random snelheid
# printen snelheidsmeting
# opvragen max_snelheid
# filteren van overtredingen

#random snelheden
dict_snelheden = registreer_snelheidsmeting(list_docenten)
print(dict_snelheden)

#printen snelheidsmeting
print_snelheden_personen("Graaf karel de goedelaan", dict_snelheden)

#stap3
max_snelheid = int(input("Wat is de maximum snelheid in de betrokken straat? "))

#filteren van overtredingen
dict_overtredingen = filter_overtredingen(max_snelheid, dict_snelheden)
print(dict_overtredingen)


#boetes uitprinten
dict_boetes = print_boetes(dict_overtredingen)
print(dict_boetes)