# Schrijf een functie ‘geef_populariteit_landen’ met als parameters bovenstaande dictionary.
# De functie geeft een nieuwe dictionary terug waarbij de landen de keys zijn, en de values
# telkens het aantal bezochte personen. Print nadien alles netjes af.
from typing import Dict, List

def geef_populariteit_landen(dict_reizigers:[str, List[str]]) -> Dict[str,int]:
    dict_resultaat = {}
    for list_landen in dict_reizigers.values():
        #overloop elke land
        for land in list_landen:
            #controle: pas aantal in dictionary aan
            if land not in dict_resultaat.keys():
                dict_resultaat[land] = 1
            else:
                dict_resultaat[land] = dict_resultaat[land] + 1
        
    return dict_resultaat






mijn_team = {
    "Stijn": ["Frankrijk", "Zwitserland", "Oostenrijk", "Nederland"],
    "Christophe": ["USA", "Frankrijk", "Duitsland"],
    "Dieter": ["Nederland", "Duitsland", "Zwitserland", "Oostenrijk"],
    "Gilles": ["UK", "Spanje", "Portugal", "Frankrijk", "Nederland"],
    "Marie": ["USA", "Spanje", "Lichtenstein", "Vaticaanstad"]
}

dict_resultaat = geef_populariteit_landen(mijn_team)

for naam_land, aantal in dict_resultaat.items():
    print(f"land: {naam_land} -> aantal: {aantal}")
