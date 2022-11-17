import functies as f

"""b = int(input("geef de basis"))
h = int(input("geef de hoogte"))
d = int(input("geef de diepte"))


f.tekst_in_kleur(str(f.inhoud_balk(b,h,d)),"groen")"""

"""print(f.willekeurige_getallen(10,10,50)) #druk een hele lijst af
for x in f.willekeurige_getallen(10,1,15): #druk ieder element van de lijst afzonderlijk af
    print(x)"""

"""lijst = f.willekeurige_getallen(100,20,10000)
lijst.sort()
lijst.reverse()
print(lijst)"""
totaal = int(input("op hoeveel gaat de test"))
for i in range(0,5):#vraagt vijf getal
    x = int(input("geef punt op 20"))
    f.toon_resultaat(x,totaal)
