"""""

#oefening 1


a = 5
b = 8
c = 9

som = a+b+c
print("{} + {} + {} = {} ".format(a,b,c,som))

"""

"""

#oefening 2

a = 6
b = 9
c = 5
d = 20

gem = (a+b+c+d)/4 #haakjes gebruiken alles op te tellen
#print(gem)

print_lijn = "het gemiddelde van {} + {} + {} + {} = {}".format(a,b,c,d,gem) #string output

print(print_lijn)

"""
"""
#formule (lengte + breedte)*2

l = 8
b = 4

omtrek = (l+b)*2

print_lijn = (l+b)*2

print("omtrek van rechthoek met lengte '{}' en breedte '{}' is '{}' ".format(l,b,(l+b)*2))
print("omtrek van rechthoek met lengte '{}' en breedte '{}' is '{}' ".format(l,b,print_lijn))

"""
"""
#input oefening

a = int(input("geef je getal in  "))
b = int(input("geef je getal in  "))

som = a+b

print("{} + {} = {} ".format(a,b,som))

"""

""""
#euro dollar converter

euro = float(input("geef je bedrag in euro in  "))
dollar = euro*0.98
print("€{} = ${})".format(euro,dollar))


"""
import math
x = 48
v = math.sqrt(x)
v1 = int(math.sqrt(x))
v2 = float(int(math.sqrt(x)))
print(v,v1,v2)


y = 7.4585
print(math.ceil(y))
print(math.floor(y))
y2 = round(y,2) #round(variable, aantal decimale)
print(y2)
print(5**2)
print(math.pow(5,2))
