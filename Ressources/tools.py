import numpy as np

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
