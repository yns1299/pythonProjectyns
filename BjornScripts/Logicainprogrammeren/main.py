geslacht = input("geef het geslacht")
leeftijd = int(input("geef de leeftijd"))
ras = input("geef het ras")

if (geslacht == "man" and leeftijd > 5) or ras =="poedel":
    print("Moet vaccinatie krijgen") # 1
else:
    print("Moet geen vaccinatie krijgen")# 0


