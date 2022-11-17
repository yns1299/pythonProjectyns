

km = float(input("geef het aantal km in "))
prijs = 0
if km < 26:
    prijs = km*0.25
else:
    km = km - 25
    prijs = 6.25+km*0.15
print("prijs : € {}".format(round(prijs,2)))
