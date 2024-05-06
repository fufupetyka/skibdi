from random import *

class Verseny:
    def __init__(self, ev, orszag, varos, arany, ezust, bronz):
        self.ev = ev
        self.orszag = orszag
        self.varos = varos
        self.arany = arany
        self.ezust = ezust
        self.bronz = bronz

cicanevek:list[str] = ['Áfonya', 'Apolló', 'Apacs', 'Babett', 'Britney', 'Borsó', 'Crazy', 'Csipesz', 'Doris', 'Espresso', 'Elektra', 'Falánk', 'Gomez', 'Hópihe', 'Hilton', 'Írisz', 'Kása', 'Lidérc', 'Love', 'Lucifer', 'Masni', 'Misa', 'Mugli', 'Nárcisz', 'Nelson', 'Pocok', 'Picur', 'Rubin', 'Szurok', 'Szüttyő', 'Tigris', 'Tepsi', 'Úrfi', 'Vanília', 'Yoda', 'Zselé', 'Zakó', 'Zeusz']

def f01() -> None:
 sz1 = int(input("Első szám: "))
 sz2 = int(input("Második szám: "))

 eredmeny = abs(sz1 - sz2)
 print(f"A két szám különbségének abszolút értéke: {eredmeny}")

 if eredmeny % 3 == 0:
    print("Osztható 3-al")
 else:
    print("Nem osztható 3-al")

def f02() -> None:
 rn:str = choice(cicanevek)

 e = 0
 for c in rn.lower():
    if c == 'e':
        e += 1
 print(f"Választott cicanév: {rn}; e betük száma: {e}")

 while input("Tetszik a név?: ") != 'igen':
    print(f'új név: {choice(cicanevek)}')
 print("Gratulálok, hello!")

def f03() -> None:
 aranyermek = 0
 versenyek = []
 ermek = 0
 file = open("paralimpia.txt", "r", encoding="utf-8")
 for sor in file:
    lista = sor.strip().split(";")
    v = Verseny(lista[0], lista[1], lista[2], int(lista[3]), int(lista[4]), int(lista[5]))
    ermek += (v.arany + v.ezust + v.bronz)
    versenyek.append(v)
    if v.arany > 0:
       aranyermek += 1
 file.close()

 print(f"Eddig {len(versenyek)} verseny volt")
 print(f"Az első versenyt ebben az orszagban tartottak: {versenyek[0].orszag}")
 print(f"Osszesen a magyarok ennyi ermet szereztek: {ermek}")
 print(f"Osszesen ennyi aranyermet szereztek legalabb: {aranyermek}")