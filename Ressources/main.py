import tools
import galeshapley as gs
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
gs.galeShapley2(listeEtu, listeSpe, capSpe)
# t= time()-t
# print(t)


gs.galeShapley(listeEtu, listeSpe, capSpe)
