import tools
import galeshapley as gs
import generatePref as gp
import matplotlib.pyplot as plt
from time import *

listeEtu=tools.lectureEtu("PrefEtu.txt")

# print(maListe)

# print(len(maListe)) #Longueur de la liste.

specap = tools.lectureSpe("PrefSpe.txt")
listeSpe = specap[0]
capSpe = specap[1]

# print(maList[0])
# print(len(maList[0])) 


# print(type((maList[0])[0][0])) #Type de l'element d'indice 0 de la liste d'indice 0
# exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier

# t = time()
# for i in range(0, 100000):
# t= time()-t
# print(t)

aff1 = gs.galeShapley(listeEtu, listeSpe, capSpe)
aff2 = gs.galeShapley2(listeEtu, listeSpe, capSpe)

print(aff1)
print(gs.testInstable(aff1, listeEtu, listeSpe))

aff1 : dict[int, list[int]]
rm0 = aff1[8].pop()
rm1 = aff1[7].pop()
rm2 = aff1[0].pop()
aff1[8].append(rm2)
aff1[7].append(rm0)
aff1[0].append(rm1)
print(gs.testInstable(aff1, listeEtu, listeSpe))
print(aff1)


lstn = []
lsttemps1 = []
lsttemps2 = []
for i in range(200, 2000, 200):
    capSpe = [i//9, i//9, i//9, i//9, i//9, i//9, i//9, i//9, i//9 + i%9]
    lstn.append(i)

    t = time()
    for _ in range(10):
        gs.galeShapley(gp.generatePrefEtu(i), gp.generatePrefSpe(i), capSpe)
    t = time() - t
    lsttemps1.append(t/10)

    t2 = time()
    for _ in range(10):
        gs.galeShapley(gp.generatePrefEtu(i), gp.generatePrefSpe(i), capSpe)
    t2 = time() - t2
    lsttemps2.append(t2/10)

plt.plot(lstn, lsttemps1, label="galeShapley")
plt.plot(lstn, lsttemps2, label="galeShapley2")
plt.legend()
plt.show()
