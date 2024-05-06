from module import *

f01()
f02()

#feladat3
versenyek:list[Verseny] = []
file = open('paralimpia.txt', 'r', encoding='utf-8')
for r in file: 
    versenyek.append(Verseny(r))

print(f'eddig {len(versenyek)} alkalommal kerult megrendezesre')

print(f'eloszor {versenyek[0].orszag} rendezett paralimpiat')

oe = 0
for v in versenyek:
    oe += (v.arany + v.ezust + v.bronz)
print(f'a magyarok összesen {oe} ermet szereztek.')

va = 0
for v in versenyek:
    if v.arany > 0:
        va += 1
print(f'a magyarok {va} versenyen szereztek legalabb egy aranyat.')

mi = 0
for i in range(1, len(versenyek)):
    if versenyek[i].arany > versenyek[mi].arany:
        mi = i
print(f'az {versenyek[mi].varos}i paralimpian szereztek a magyarok legtöbb aranyat')

ke = int(input('írj be egy evszamot: '))
for v in versenyek:
    if v.ev == ke:
        print(f'a {v.ev} ban/ben a paralimpiat {v.orszag} szervezte')
        break
else:
    print(f'{ke} evben nem volt paralimpia')

evek:list[int] = []
for v in versenyek:
    if v.arany == 0 and v.ezust == 0 and v.bronz == 0:
        evek.append(v.ev)
print(f'ebben az evben nem voltak helyezesek {evek}')