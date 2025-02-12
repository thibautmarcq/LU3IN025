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
    aff1 = gs.galeShapley(listeEtu, listeSpe, capSpe)[0]
    aff2 = gs.galeShapley2(listeEtu, listeSpe, capSpe)[0]
    print("Affectations côté étudiants GS > ", aff1)
    print("Affectations côté parcours GS > ", aff2)
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
    print("Test instabilité après déréglage \n > ", gs.testInstable(aff1, listeEtu, listeSpe))
    print("Affectations avec paires instables \n > ", aff1)

    # Création du PLNE
    tools.createkPLNE(3, listeEtu, capSpe, "Results/main.lp")

    # Génération des graphiques pour la complexité
    lstiter1 = []
    lstiter2 = []
    lstn = []
    lsttemps1 = []
    lsttemps2 = []
    moyenne = 20
    for i in range(200, 2001, 200):
        capSpe = [i//9, i//9, i//9, i//9, i//9, i//9, i//9, i//9, i//9 + i%9]
        lstn.append(i)
        
        # ttot1 = 0.0
        # ttot2 = 0.0

        for _ in range(moyenne):
            prefEtu = tools.generatePrefEtu(i)
            prefSpe = tools.generatePrefSpe(i)
            t = time()
            gs.galeShapley(prefEtu, prefSpe, capSpe)
            t = time() - t
            ttot1 += t

            t2 = time()
            gs.galeShapley2(prefEtu, prefSpe, capSpe)
            t2 = time() - t2
            ttot2 += t2

        lsttemps1.append(ttot1/moyenne)
        lsttemps2.append(ttot2/moyenne)
        
        lstiter1.append(gs.galeShapley(prefEtu, prefSpe, capSpe)[1])
        lstiter2.append(gs.galeShapley2(prefEtu, prefSpe, capSpe)[1])
        
        
    # plt.plot(lstn, lsttemps1, label="galeShapley")
    # plt.plot(lstn, lsttemps2, label="galeShapley2")
    # plt.xlabel("Nombre n d'étudiants")
    # plt.ylabel("Temps de calcul moyen")
    # plt.legend()
    # plt.show()
    # plt.savefig('Results/evolution_temps.svg')

    # Sur les itérations
    plt.plot(lstn, lstiter1, label="galeShapley")
    plt.plot(lstn, lstiter2, label="galeShapley2")
    plt.xlabel("Nombre n d'étudiants")
    plt.ylabel("Nombre d'itérations")
    plt.legend()
    # plt.show()
    plt.savefig('Results/evolution_iterations.svg')
    
    
if __name__ == "__main__":
    main()