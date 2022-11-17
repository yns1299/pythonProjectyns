getallen = []
for i in range(1,11):
    invoer = int(input("geef het getal in "))
    getallen.append(invoer)
print(getallen,sum(getallen))
print("de getallen zijn {} de som van de lijst is {}".format(getallen,sum(getallen)))
