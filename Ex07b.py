# zin = "Dit is Howest, is het niet zo? Uiteraard, welkom!"
# print(f"Onderzochte zin:\n{zin}\n")
# dic_woorden = tel_voorkomen_woorden(zin)


# Maak een functie ‘tel_voorkomen_woorden’ met als parameter een string. De functie geeft
# een dictionary terug waarbij de keys de verschillende woorden uit de zin zijn en de bijhorende
# values het aantal keer is dat het woord in de zin voorkomt. Print nadien de dictionary af.

from typing import Dict


def tel_voorkomen_woorden(zin:str) -> Dict[str,int]:
    dictionary_result = {}

    #leestekens uit zin verwijderen
    zin = zin.replace("!"," ")
    zin = zin.replace(","," ")    
    zin = zin.replace("?"," ")
    zin = zin.replace(";"," ")
    zin = zin.replace(":"," ")

    for woord in zin.split(" "):
        woord = woord.lower()   #zet om naar kleine letters
        if woord not in dictionary_result:
            dictionary_result[woord] = 1
        else:
            dictionary_result[woord] = dictionary_result[woord] + 1

    return dictionary_result



zin = "Dit is Howest, is het niet zo? Uiteraard, welkom aan Howest!"
print(f"Onderzochte zin:\n{zin}\n")
dic_woorden = tel_voorkomen_woorden(zin)
print(dic_woorden)