from colorama import Fore
import random as r

def inhoud_balk(b,h,d): #8 4 10
    return b*h*d #320

def tekst_in_kleur(tekst,kleur):
    if kleur.lower()== "blauw":
        print(Fore.BLUE+tekst)
    elif kleur.lower()== "groen":
        print(Fore.GREEN+tekst)
    elif kleur.lower()== "rood":
        print(Fore.RED+tekst)
    else:
        print(Fore.WHITE+tekst)

def tussen_tien_en_honderd(x):
    if x > 10 and x < 100:
        return True
    else:
        return False

def willekeurige_getallen(aantal_getallen,begin,eind):
    getallen = [] #lijst
    for i in range(0,aantal_getallen):
        if(begin < eind):
            getallen.append(r.randint(begin,eind))
        else:
            getallen.append(r.randint(eind,begin))
    return getallen

def toon_resultaat(score,max):
    if score > max:
        print(Fore.RED+"ongeldige invoer")
        print(Fore.RESET)
    else:
        procent = score/max*100
        if procent > 80:
            print(Fore.GREEN+str(procent))
        elif procent >50 and procent < 80:
            print(Fore.RESET+str(procent))
        else:
            print(Fore.RED+str(procent))

