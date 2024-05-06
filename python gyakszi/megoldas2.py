from datetime import datetime

#3.feladat [B]
class Film:
    def __init__(self,filmcim, fazis, datum, koltseg, bevetel):
        self.filmcim = filmcim,
        self.fazis = int(fazis),
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

osszesen = 0
for film in filmek:
    if film.fazis[0] < 3:
        osszesen += 1
print(f"3.2: a 3. fázis előtti filmek száma: {osszesen}db")

film = filmek[0]
for i in filmek:
    if (i.bevetel - i.koltseg) < (film.bevetel - film.koltseg):
        film = i
    else:
        continue
print(f"3.3: a legalacsonyabb hasznot a(z): {film.filmcim[0]} c. film hozta")

cimreszlet = input("3.4: írjon be egy címrészletet: ")

for film in filmek:
    if cimreszlet in film.filmcim[0]:
        print(f"\t{film.filmcim[0]}")