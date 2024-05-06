from random import *

class Verseny:
  def __init__(self, row:str) -> None:
    v:list[str] = row.strip().split(';')
    self.ev = int(v[0])
    self.orszag:str = v[1]
    self.varos:str = v[2]
    self.arany:int = int(v[3])
    self.ezust:int = int(v[4])
    self.bronz:int = int(v[5])


cicanevek:list[str] = ['Áfonya', 'Apolló', 'Apacs', 'Babett', 'Britney', 'Borsó', 'Crazy', 'Csipesz', 'Doris', 'Espresso', 'Elektra', 'Falánk', 'Gomez', 'Hópihe', 'Hilton', 'Írisz', 'Kása', 'Lidérc', 'Love', 'Lucifer', 'Masni', 'Misa', 'Mugli', 'Nárcisz', 'Nelson', 'Pocok', 'Picur', 'Rubin', 'Szurok', 'Szüttyő', 'Tigris', 'Tepsi', 'Úrfi', 'Vanília', 'Yoda', 'Zselé', 'Zakó', 'Zeusz']


def f01() -> None:
 szam1 = int(input("Írj be egy számot: "))
 szam2 = int(input("Írj be egy számot: "))

 e = abs(szam1 - szam2)
 print(f'A két szám különbségének abszolút értéke: {e}')

 if e % 3 == 0:
    print("Osztható 3-al")
 else:
    print("Nem osztható 3-al")

def f02() -> None:
 rcn:str = choice(cicanevek)

 e = 0
 for c in rcn.lower():
    if c == 'e': 
        e += 1
    
 print(f'választott cicanév: {rcn}; e betük száma: {e};')

 while input('Tetszik a név?: ') != 'igen':
   print(f'új név: {choice(cicanevek)}')
 print('Gratulálok, szia!')

