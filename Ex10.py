#  Gegeven een dictionary waarbij de keys verschillende personen voorstellen en de values de
# bijhorende landen die bezocht werden.

# Schrijf een functie ‘filter_op_land’ met als parameters bovenstaande dictionary en een
# gezocht land. De functie geeft in een list alle personen terug die dit land bezocht hebben.

from typing import Dict, List

#parameters zijn bijzonder:
# eerste parameter is een dictionary waarvan de keys strigns zijn, en de values zijn een list van strings
def filter_op_land(dict_reizigers:Dict[str,List[str]], gezocht_land:str) -> List[str]:
    betrokken_reizigers = []
    for persoon, list_landen in dict_reizigers.items():
        #controle: zit het gezochte land in de list_landen
        if gezocht_land in list_landen:
            #bingo -> de persoon is naar dat land geweest
            betrokken_reizigers.append(persoon)
    



    return betrokken_reizigers





mijn_team = {
    "Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
    "Christophe": ["USA", "Frankrijk", "Duitsland"],
    "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
    "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"],
    "Marie": ["USA", "Spanje", "Lichtenstein", "Vaticaanstad"]
}
gezocht_land = input("Geef een land op:> ")
namen = filter_op_land(mijn_team, gezocht_land)
print(f"Deze personen hebben reeds dit land bezocht: {namen}")



