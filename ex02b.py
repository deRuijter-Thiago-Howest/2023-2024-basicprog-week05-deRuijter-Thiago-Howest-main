from typing import Tuple

def print_tuple(naam_tuple:str,tuple_elementen:Tuple) -> None:
    print(f"verzameling {naam_tuple}:")
    teller = 0
    for element in tuple_elementen:
        print(f"{element} zit op positie {teller}")
        teller += 1



t1 = ("1mct", "2mct", "3mct")
t2 = ("1ctai", "2ctai")
t3 = ("test", True, 3.2, 1)


print_tuple("MCT",t1)
print_tuple("CTAI",t2)
print_tuple("Van alles",t3)

#index -> als element niet gevonden wordt => uitvoeringsfout (valueerror)
# print(f"Test: {t1.index("4mct")}")
