import functies_oppervlakte as f
print("keuze 1 vierkant, 2 rechthoek, 3 driehoek, 4 cirkel, 5 stop")
keuze = ""
while (keuze != "stop"):
    keuze = input("kies uw keuze")
    if keuze == "1":
        z = int(input("geef de zijde in "))
        f.oppervlakte_vierkant(z)
    elif keuze =="2":
        b = int(input("geef de basis in "))
        h = int(input("geef de hoogte in "))
        f.oppervlakte_rechthoek(b,h)
    elif keuze =="3":
        b = int(input("geef de basis in "))
        h = int(input("geef de hoogte in "))
        f.oppervlakte_driehoek(b,h)
    elif keuze =="4":
        r = int(input("geef de straal in"))
    elif keuze =="5":
        break
    else:
        print("verkeerde input")
    print("keuze 1 vierkant, 2 rechthoek, 3 driehoek, 4 cirkel, 5 stop")

