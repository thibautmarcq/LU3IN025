import tools
import galeshapley as gs

maListe=tools.lectureEtu("PrefEtu.txt")
print(maListe)

print(len(maListe)) #Longueur de la liste.

maList=tools.lectureSpe("PrefSpe.txt")
print(maList[0])
print(len(maList[0])) 


print(type((maList[0])[0][0])) #Type de l'element d'indice 0 de la liste d'indice 0
# exemple.createFichierLP(maListe[0][0],int(maListe[1][0])) #Methode int(): transforme la chaine de caracteres en entier

# gs.galeShapley(maListe,maList)
