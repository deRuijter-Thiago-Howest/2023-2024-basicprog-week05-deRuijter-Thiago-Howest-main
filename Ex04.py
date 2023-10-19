# print("Dictionary ....")
# print("Key: .... -> value: ....")
# Maak nu één functie ‘print_dictionary’ die de verschillende elementen overloopt waarbij
# telkens key & value samen op één lijn worden afgeprint.
# De functie heeft als parameters een naam (voor de dictionary) en de dictionary zelf.
# Voorbeeld
from typing import Dict


def print_dictionary(naam_dict:str,elementen:Dict) -> None:
    for key,value in elementen.items():
        print(f"De Value van volgende key van dictionary {naam_dict} is: {key}  ->  {value} ")




Getallen = {"getal1": 46, "getal2": 57, "getal3": 3.6 }


print_dictionary("dictgetal", Getallen)