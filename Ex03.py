# Maak volgende 3 dictionaries aan.
# Ze stellen beide de verschillende studentenaantallen per opleidingsjaar voor.
# - ‘ctai’ met de elementen {"1CTAI": 58, "2CTAI": 36}
# - ‘mct’ met de elementen {"1MCT": 131, "2MCT": 88, "3MCT": 77}
# - ‘devine’ met de {"1Devine": 123, "2Devine": 98, "3Devine": 55}
# Geef een antwoord op onderstaande vragen d.m.v. een kort codevoorbeeld op bovenstaande
# dictionaries:
# - Wat is het effect van het print-commando op een dictionary?
# - Hoe kan je een element uit de dictionary opvragen?
# - Hoe voeg je een nieuw element aan een dictionary toe?
# - Wat gebeurt er als een nieuw element met dezelfde key aan een dictionary
# toegevoegd wordt?
# - Hoe controleer je of een key in een dictionary reeds in gebruik is?
# - Hoe kan je een key (met value) uit een dictionary verwijderen?
# Wat als key niet aanwezig is?

CTAI = {"1CTAI": 58, "2CTAI": 36}
MCT = {"1MCT": 131, "2MCT": 88, "3MCT": 77}
devine = {"1Devine": 123, "2Devine": 98, "3Devine": 55}

# - Wat is het effect van het print-commando op een dictionary?

print(CTAI)            #het wordt afgeprint, samen met de keys.


# - Hoe kan je een element uit de dictionary opvragen?
print(f"Het aantal elementen in 2mct is : {MCT['2MCT']}")


#Hoe voeg je een nieuw element aan een dictionary toe?

CTAI["3CTAI"] = 25
print(CTAI)


# - Wat gebeurt er als een nieuw element met dezelfde key aan een dictionary
# toegevoegd wordt?

CTAI["3CTAI"] = 100                  #de key wordt aangepast
print(CTAI)


# - Hoe controleer je of een key in een dictionary reeds in gebruik is?

if "1Devine" in devine.keys():
    print("De key 3Devine is in gebruik")
else:
    print("De key is nog niet in gebruik")

# - Hoe kan je een key (met value) uit een dictionary verwijderen?

# del(devine["2Devine"])  
# del(devine["2Devine"])                  #double verwijderen kan niet => keyerror!! (key niet in dictionary gebruikt wordt)
print(devine)




#printen van enkel de values:

print("Dit zijn de values uit de dictionary MCT")
for value in MCT.values():
    print(value)

#printen van keys en values samen:
for key, value in MCT.items():
    print(f"{key} -> {value}")