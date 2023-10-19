# Maak een nieuwe lege dictionary ‘Howest’ aan.
# Voeg bovenstaande dictionaries eraan toe.
from typing import Dict


def print_dictionary(naam_dict:str,elementen:Dict) -> None:
    for key,value in elementen.items():
        print(f"De Value van volgende key van dictionary {naam_dict} is: {key}  ->  {value} ")




Getallen = {"getal1": 46, "getal2": 57, "getal3": 3.6 }


Howest = {}
CTAI = {"1CTAI": 58, "2CTAI": 36}
MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}


#versie 1
# Howest = CTAI | devine | MCT

#versie 2

Howest.update(MCT)
Howest.update(CTAI)
Howest.update(devine)

print_dictionary("Howest",Howest)