# Maak een pythonapplicatie die in staat is om de binnengekomen feedbackscores (van een
# evenement) te verwerken. Hierbij wordt aan een medewerker gevraagd alle feedbackscores
# één voor één in te geven. De medewerker kan afsluiten met een lege score. Op het einde
# worden de scores geteld en afgeprint.
# Geef de verschillende evaluatiecijfers door (sluit af met lege waarde)

evaluaties = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
print("Geef de verschilleden evaluatiecijfers door (sluit af met lege waarde)")
print("Uitmuntend: A, Zeer goed: B, Goed: C, Voldoende: D, Onvoldoende: E, Zwak: F")
score = input("Geef de nieuwe feedbackscore op :> ")
while score != "":
    score = score.upper()

    #controle

    # if score in ["A", "B", "C", "D", "E", "F"]:
    if score in evaluaties.keys():
        #score verwerken -> de value bij de juiste key in de dictionary verhogen
        evaluaties[score] = evaluaties[score] + 1 
    else:
        print("ongeldige score, probeer opnieuw")
    

    #nieuwe score opvragen
    score = input("Geef de nieuwe feedbackscore op:> ")


print("De gegevens zijn verwerkt. Dit is het resultaat")
for key, value in evaluaties.items():
    print(f"score {key} -> aantal:{value}")
