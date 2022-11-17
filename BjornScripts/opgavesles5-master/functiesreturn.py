def ok(g,l,r):
    if(g.upper()=="VROUW" and l>=18 and r=="nee"):
        return True
    else:
        return False

geslacht = input("geef het geslacht")
leeftijd = int(input("geef leeftijd"))
rijbewijs =input("rijbewijs ja/nee")
if ok(geslacht,leeftijd,rijbewijs):
    print("Het is in orde")
else:
    print("Het is niet in orde")
