# Maak een methode ‘voeg_nieuw_element_toe’ die een nieuw element aan een dictionary
# toevoegt nadat er eerst gecontroleerd wordt of de key nog niet in gebruik is. Indien de key
# wel al in gebruik is, wordt er een foutboodschap afgeprint. De methode heeft als parameters
# de key, de value en de dictionary zelf.
# Test dit uit door aan dictionary Howest achtereenvolgens toe te voegen
# - Element met key ‘1IPO’ met waarde ‘51’
# - Element met key ‘1IPO’ met waarde ‘10’
# Print nadien de dictionary Howest af (via methode uit eerdere oefening).


from typing import Dict


def print_dictionary(naam_dict:str,elementen:Dict[str,int]) -> None:
    for key,value in elementen.items():
        print(f"De Value van volgende key van dictionary {naam_dict} is: {key}  ->  {value} ")


#opmerking: bij een dictionary kan je ook vermelden wat het datatype van de keys en values zijn
#in deze functie -> de keys zijn strings , de values zijn ints
def voeg_nieuw_element_toe(key: str, value: int, elementen: Dict[str,int]) -> None:      
    if key in elementen.keys():
        print(f"Foutmelding: de key:{key} is al in gebruik")
    else:
        elementen[key] = value
        print("toevoegen is wel gelukt")





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
voeg_nieuw_element_toe("1IPO", 100, Howest)
voeg_nieuw_element_toe("2IPO", 67, Howest)
print(Howest)