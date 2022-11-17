import random

getal1 = random.randint(1,1000)
getal2 = random.randint(1,1000)
getal3 = random.randint(1,1000)
getal4 = random.randint(1,1000)

if getal1 > getal2 and getal1 > getal3 and getal1 > getal4: print("het eerste getal is het grootste")
if getal2 > getal1 and getal2 > getal3 and getal2 > getal4: print("het tweede getal is het grootste")
if getal3 > getal1 and getal3 > getal2 and getal3 > getal4: print("het derde getal is het grootste")
if getal4 > getal1 and getal4 > getal2 and getal4 > getal3: print("het derde getal is het grootste")

print("eind")
