import numpy as np
import random

def lectureEtu(s): 
	monFichier = open(s, "r")
	contenu = monFichier.readlines()
	monFichier.close() 
	res=np.empty(shape=(int(contenu[0]),9), dtype=int)

	for i in range(1, int(contenu[0])+1):
		contenu[i] = contenu[i].split()
		res[i-1] = contenu[i][2:]
	return res

def lectureSpe(s): 
	monFichier = open(s, "r")
	contenu = monFichier.readlines()
	monFichier.close() 
	contenu[0] = contenu[0].split()
	res = np.empty(shape=(9,int(contenu[0][1])), dtype=int)
	contenu[1] = contenu[1].split()
	cap = contenu[1][1:]
	cap = np.array(cap).astype(int)
	
	for i in range(2, 11):
		contenu[i] = contenu[i].split()
		res[i-2] = contenu[i][2:]
	return (res,cap)


def generatePrefEtu(n : int):
	prefs = []
	for _ in range(n):
		pref = list(range(9))
		random.shuffle(pref)
		prefs.append(pref)
	return prefs
	   
def generatePrefSpe(n: int):
	prefs = []
	for _ in range(9):
		pref = list(range(n))
		random.shuffle(pref)
		prefs.append(pref)
	return prefs

def createPLNE(k : int, prefEtu, capSpe):
	f = open("fichier.lp", "w")
	f.write("Maximize\nobj: ")
	l = [] #liste des variables
	l2 = {} #dico clé:spé, valeur:liste des variables xi_j avec i étudiant et j clé spé
	lenEtu = prefEtu.shape[0] #nombre d'étudiants
	for i in range(lenEtu):
		for j in range(k):
			s = "x"+str(i)+"_"+str(prefEtu[i][j]) #nom des variable
			l.append(s)
			if prefEtu[i][j] not in l2:
				l2[prefEtu[i][j]] = []
			l2[prefEtu[i][j]].append(s)

			if(i==lenEtu-1 and j==k-1): #dernier élément
				f.write(s)
			else : 
				f.write(s+" + ")

	f.write("\nSubject To\n")
	tmp = 1 #compteur pour les contraintes
	for i in range(len(l)): 
		if(i%k==0): 
			f.write("c"+str(tmp)+": ")
			tmp+=1
		if((i+1)%k==0): #dernier élément de la contrainte
			f.write(l[i]+" <= 1\n")
		else:
			f.write(l[i]+" + ")

	for key, value in l2.items(): 
		f.write("c"+str(tmp)+": ") #contrainte de capacité
		lenSpe = len(value)
		for i in range(lenSpe-1):
			f.write(value[i]+" + ")
		f.write(value[lenSpe-1]+" <= "+str(capSpe[key])+"\n") 
		tmp += 1

	f.write("Binary\n")
	for i in range(len(l)): #variables binaires
		f.write(l[i]+" ")
	
	f.write("\nEnd")
	f.close()