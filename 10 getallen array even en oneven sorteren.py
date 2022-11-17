lijst_even = []
lijst_oneven = []

for i in range(1,11):
    invoer = int(input("geef het getal in "))
    if invoer %2==0:
        lijst_even.append(invoer)
    else:
        lijst_oneven.append(invoer)

print("even",lijst_even)
print("oneven",lijst_oneven)
