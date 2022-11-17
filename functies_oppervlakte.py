import math
def oppervlakte_vierkant(z):
    print(z**2)
def oppervlakte_rechthoek(b,h):
    print(b*h)
def oppervlakte_driehoek(b,h):
    print(b*h/2)
def oppervlakte_circel(r):
    print(round(r**2*math.pi,2)) #afronden tot 2cijfers na komma
def inhoud_balk(b,h,d):
    return b*h*d

#oppervlakte_vierkant(5)
#oppervlakte_rechthoek(4,5)
#oppervlakte_driehoek(4,8)
#oppervlakte_circel(5)

#inhoud balk -> "functie balk.py"
