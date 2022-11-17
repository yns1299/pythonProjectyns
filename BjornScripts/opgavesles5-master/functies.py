from colorama import Fore


def dubbelofhelft(x):
    if x % 2 == 0:
        print(x / 2)
    else:
        print(x * 2)


def zeg_naam(naam):
    print(naam)


def zeg_tekst_hoofdletter_groen(tekst):
    print(Fore.GREEN + tekst.upper())


def zeg_tekst_hoofdletter_groen_blauw(tekst, kleur):
    if kleur == "Groen":
        print(Fore.GREEN + tekst.upper())
    elif kleur == "Blauw":
        print(Fore.BLUE + tekst.upper())
    else:
        print(tekst)


def zet_in_hoofdletters(tekst):
    print(tekst.upper())


zeg_tekst_hoofdletter_groen_blauw("Dit is een banaan", "Groen")
