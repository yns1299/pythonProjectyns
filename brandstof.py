aantal_litter = float(input("geef het aantal liter in "))
brandstof = input("benzine of diesel, b of d")
if brandstof.lower() == "b":
    print(aantal_litter*1.75)
elif brandstof.lower() == "d":
    print(aantal_litter*1.95)
else:
    print("fout ingave")

