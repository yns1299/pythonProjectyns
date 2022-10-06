import math

straal = int(input("geef de straal in "))
hoogte = int(input("geef de hoogte in "))
print("Straal:\t{}\nHoogte:\t{}\ninhoud\t{}m³".format(straal,hoogte,round(straal**2*math.pi*hoogte,2)))
