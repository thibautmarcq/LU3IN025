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

def createkPLNE(k : int, prefEtu, capSpe, outFile):
	f = open(outFile, "w")
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


def borda(pref_etu, pref_spe) :
	nb_etu = len(pref_etu)
	nb_spe = len(pref_spe)

	borda_etu_spe = [ [-1 for _ in range(nb_spe) ] for _ in range(nb_etu) ]
	borda_spe_etu = [ [-1 for _ in range(nb_etu) ] for _ in range(nb_spe) ]
	borda_sum = [ [-1 for _ in range(nb_etu) ] for _ in range(nb_spe) ]

	for etu in range(nb_etu) :
		for ind in range(nb_spe) :
			spe = pref_etu[etu][ind]
			borda_etu_spe[etu][spe] = nb_spe - ind - 1

	for spe in range(nb_spe) :
		for ind in range(nb_etu) :
			etu = pref_spe[spe][ind]
			borda_spe_etu[spe][etu] = nb_etu - ind -1

	for i in range(nb_spe):
		for j in range(nb_etu):
			borda_sum[i][j] = borda_etu_spe[j][i] + borda_spe_etu[i][j]

	return borda_sum


def createEffiPLNE(borda , capSpe, outFile):
	f = open(outFile, "w")
	f.write("Maximize\nobj: ")
	l = [] #liste des variables

	nbEtu = len(borda) #nombre d'étudiants
	nbSpe = len(borda[0])
	for i in range(nbEtu):
		for j in range(nbSpe):
			s = "x"+str(i)+"_"+str(j) #nom des variable
			l.append(s)
			if(i==nbEtu-1 and j==nbSpe-1): #dernier élément
				f.write(str(borda[i][j])+" "+s)
			else : 
				f.write(str(borda[i][j])+" "+s+" + ")

	f.write("\nSubject To\n")
	tmp = 1 #compteur pour les contraintes
	for i in range(len(l)): 
		if(i%nbSpe==0): 
			f.write("c"+str(tmp)+": ")
			tmp+=1
		if((i+1)%nbSpe==0): #dernier élément de la contrainte
			f.write(l[i]+" = 1\n")
		else:
			f.write(l[i]+" + ")

	for i in range(nbSpe):
		f.write("c"+str(tmp)+": ")
		tmp+=1
		for j in range(nbEtu):
			if(j==nbEtu-1): #dernier élément
				f.write("x"+str(j)+"_"+str(i)+" = "+str(capSpe[i])+"\n")
			else : 
				f.write("x"+str(j)+"_"+str(i)+" + ")


	f.write("Binary\n")
	for i in range(len(l)): #variables binaires
		f.write(l[i]+" ")
	
	f.write("\nEnd")
	f.close()


def createKEffiPLNE(borda , kprefEtu, capSpe, outFile):
	f = open(outFile, "w")
	f.write("Maximize\nobj: ")
	l = [] #liste des variables
	l2 = {} #dico clé:spé, valeur:liste des variables xi_j avec i étudiant et j clé spé

	nbEtu = len(kprefEtu) #nombre d'étudiants
	nbSpe = len(kprefEtu[0])
	for i in range(nbEtu):
		for j in range(nbSpe):
			spe = kprefEtu[i][j]
			s = "x"+str(i)+"_"+str(spe) #nom des variable
			l.append(s)
			if spe not in l2:
				l2[spe] = []
			l2[spe].append(s)
			if(i==nbEtu-1 and j==nbSpe-1): #dernier élément
				f.write(str(borda[i][spe])+" "+s)
			else : 
				f.write(str(borda[i][spe])+" "+s+" + ")

	f.write("\nSubject To\n")
	tmp = 1 #compteur pour les contraintes
	for i in range(len(l)): 
		if(i%nbSpe==0): 
			f.write("c"+str(tmp)+": ")
			tmp+=1
		if((i+1)%nbSpe==0): #dernier élément de la contrainte
			f.write(l[i]+" = 1\n")
		else:
			f.write(l[i]+" + ")

	for key, value in l2.items(): 
		f.write("c"+str(tmp)+": ") #contrainte de capacité
		lenSpe = len(value)
		for i in range(lenSpe-1):
			f.write(value[i]+" + ")
		f.write(value[lenSpe-1]+" = "+str(capSpe[key])+"\n") 
		tmp += 1

	f.write("Binary\n")
	for i in range(len(l)): #variables binaires
		f.write(l[i]+" ")
	
	f.write("\nEnd")
	f.close()
