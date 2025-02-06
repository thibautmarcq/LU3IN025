import tools
import galeshapley as gs
import matplotlib.pyplot as plt
from time import *

def main():
    # Récupération des matrices de préférences des étudiants/spé et des capacités
    listeEtu = tools.lectureEtu("Ressources/PrefEtu.txt")
    speCap = tools.lectureSpe("Ressources/PrefSpe.txt")
    listeSpe = speCap[0]
    capSpe = speCap[1]

    # Affectations renvoyées côté étu et côté spé
    aff1 = gs.galeShapley(listeEtu, listeSpe, capSpe)
    aff2 = gs.galeShapley2(listeEtu, listeSpe, capSpe)

    print("Affectations 1 GS > ", aff1)
    # Test si un couple est instable parmis l'affectation de GS
    print("Test instabilité aff1 > ", gs.testInstable(aff1, listeEtu, listeSpe))

    # Modification des affectations pour détecter des couples instables
    aff1 : dict[int, list[int]]
    rm0 = aff1[8].pop()
    rm1 = aff1[7].pop()
    rm2 = aff1[0].pop()
    aff1[8].append(rm2)
    aff1[7].append(rm0)
    aff1[0].append(rm1)
    print("Test instabilité après dérèglage \n > ", gs.testInstable(aff1, listeEtu, listeSpe))
    print("Affectations avec paires instables \n > ", aff1)


    # Génération des graphiques pour la complexité
    lstn = []
    lsttemps1 = []
    lsttemps2 = []
    for i in range(200, 2000, 200):
        capSpe = [i//9, i//9, i//9, i//9, i//9, i//9, i//9, i//9, i//9 + i%9]
        lstn.append(i)

        t = time()
        for _ in range(10):
            gs.galeShapley(tools.generatePrefEtu(i), tools.generatePrefSpe(i), capSpe)
        t = time() - t
        lsttemps1.append(t/10)

        t2 = time()
        for _ in range(10):
            gs.galeShapley(tools.generatePrefEtu(i), tools.generatePrefSpe(i), capSpe)
        t2 = time() - t2
        lsttemps2.append(t2/10)

    plt.plot(lstn, lsttemps1, label="galeShapley")
    plt.plot(lstn, lsttemps2, label="galeShapley2")
    plt.xlabel("Nombre n d'étudiants")
    plt.ylabel("Temps de calcul moyen")
    plt.legend()
    plt.savefig('Results/evolution_temps_nbEtu.svg')
    plt.show()
    
    
    
if __name__ == "__main__":
    main()