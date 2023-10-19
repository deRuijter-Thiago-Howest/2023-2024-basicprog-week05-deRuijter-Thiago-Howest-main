# Maak één functie ‘print_tuple’ die de verschillende elementen overloopt waarbij elk element
# samen met zijn index wordt afgeprint. De functie heeft als parameters een naam (voor de
# tuple) en de tuple zelf.
from typing import Tuple


def print_tuple(naam_tuple:str,tuple_elementen:Tuple) -> None:
    print(f"verzameling {naam_tuple}:")
    for element in tuple_elementen:
        print(f"{element} zit op positie {tuple_elementen.index(element)}")



t1 = ("1mct", "2mct", "3mct")
t2 = ("1ctai", "2ctai")
t3 = ("test", True, 3.2, 1)


print_tuple("MCT",t1)
print_tuple("CTAI",t2)
print_tuple("Van alles",t3)

#versie 2
