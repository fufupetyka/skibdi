from datetime import datetime
def feladat(szam):
    return print("\n{}. Feladat\n".format(szam))

# feladat(1)
# karakterlanc = input("Adjon meg egy maximum 8 hosszú karakterláncot: ")
# if len(karakterlanc) > 8:
#     print("Túl hosszú a karakterlánc!")
# else:
#     print(karakterlanc[::-1])
    
# feladat(2)
# class Termek:
#     def __init__(self, nev, ar):
#         self.nev = nev
#         self.ar = ar
       
 
# termek1 = Termek("Paradicsom", 1199)
# termek2 = Termek("Paprika", 1349)
# termek3 = Termek("Vöröshagyma", 289)

# termekek = [termek1,termek2,termek3]

# for termek in termekek:
#     print("{}: {} Ft/Kg".format(termek.nev,termek.ar))

# print("\n")
# valasz = ""
# osszeg = 0
# while( valasz != "nem"):
#     valasz = input("Kíván-e vásárolni? ")
#     if(valasz != "nem"):
#         termekneve = input("\tMelyik termékből? ")
#         valasztotTermek = ""
#         vanE = False
#         for i in termekek:
#             if i.nev.lower() == termekneve.lower():
#                 valasztotTermek = i
#                 vanE = True
#             else:
#                 vanE = False
                
#         if vanE:    
#             mennyiseg = float( input(f"\tHány kg {valasztotTermek.nev}(o)t szeretne? "))
#             osszeg = mennyiseg * valasztotTermek.ar
#         else:
#             print("\tnincs ilyen termék!")
#     else:
#         print("\nköszönjük a vásárlást!\nfizetendő összeg: {:.0f}Ft".format(osszeg))       
#         continue
    
feladat(3)
class Film:
    def __init__(self,filmcim, fazis, datum, koltseg, bevetel):
        self.filmcim = filmcim,
        self.fazis = fazis,
        self.datum = datetime.strptime(datum, '%Y-%m-%d'),
        self.koltseg = float(koltseg)
        self.bevetel = float(bevetel)
        
    def __repr__(self):
        return f"{self.filmcim} {self.fazis} {self.datum} {self.koltseg} {self.bevetel}"

filmek = []
with open("marvel.txt", "r", encoding='utf-8') as file:
    for line in file:
        # film = Film(*line.strip().split(';'))
        filmcim, fazis, datum, koltseg, bevetel = line.strip().split(';')
        film = Film(filmcim, fazis, datum, float(koltseg), float(bevetel))
        filmek.append(film)
      
print("3.1: {} filmje van a marvel moziverzumának".format(len(filmek)))
print("3.2: A filmek átlagos gyártási költsége: ${:.2f}M ".format(sum(film.koltseg for film in filmek)/len(filmek)))
hatekony = filmek[0]
for film in filmek:
    if film.bevetel/film.koltseg > hatekony.bevetel/hatekony.koltseg:
        hatekony = film
    else:
        continue
print("3.3: A legköltséghatékonyabb film címe: {} ".format(hatekony.filmcim[0]))

evszam = int(input("irjon be egy évszámot: "))

print("a {}-ban/ben megjelent marvel filmek:".format(evszam))
for film in filmek:
    if film.datum[0].year == evszam:
        print(f"\t{film.filmcim[0]}")
