import numpy as np
import heapq as hq


def galeShapley(tabEtu, tabSpe, cap):
    # Initialisation
    etu_libres = list(range(len(tabEtu)))
    capSpe = cap.copy()  # list[int]
    dictEtu = {i: list(tabEtu[i]) for i in range(len(tabEtu))}  # dict etu - clé: num étu, bucket: liste pref etu (int: int)
    dictSpe = {i: list(tabSpe[i]) for i in range(len(tabSpe))}  # dict spe - clé: num spé, bucket: liste pref spé
    affectations = {}  # dico résultats, clé: num spé, bucket: liste des étu choisis dans la spé (int, int)

    while etu_libres:  # tant qu'il reste un etu libre
        num_i = etu_libres.pop()
        spe_h = int(dictEtu[num_i].pop(0))  # premier élément dans les prefs de i (retiré)

        if spe_h not in affectations:
            affectations[spe_h] = []
            hq.heapify(affectations[spe_h])

        if capSpe[spe_h] > 0:  # H n'a pas atteint sa cap max
            capSpe[spe_h] -= 1  # on diminue la capacité restante de H
            hq.heappush(affectations[spe_h], (dictSpe[spe_h].index(num_i), num_i))
        else:  # on a atteint la capacité max de la spe_H
            max_pref, worst_etu = hq.nlargest(1, affectations[spe_h])[0]  # on obtient l'etudiant le moins préféré de la spé

            idx_i = dictSpe[spe_h].index(num_i)
            if idx_i < max_pref:  # h pref I à least_pref
                affectations[spe_h].remove((max_pref, worst_etu))  # enleve le pire étudiant
                hq.heapify(affectations[spe_h])  # reconvertir en heap
                etu_libres.append(worst_etu)  # rajout du pire dans les libres
                hq.heappush(affectations[spe_h], (idx_i, num_i))  # ajout du meilleur (i)

            else:  # H rejette la proposition de i
                etu_libres.append(num_i)

    # Convert heap to sorted list for final output
    for spe_h in affectations:
        affectations[spe_h] = [etu for _, etu in sorted(affectations[spe_h])]

    # print(sorted(list(affectations.items())))
    return affectations



def galeShapley2(tabEtu, tabSpe, cap):
    spe_libres = list(range(len(tabSpe)))
    capSpe = cap.copy()
    dictEtu = {i: list(tabEtu[i]) for i in range(len(tabEtu))}
    dictSpe = {i: list(tabSpe[i]) for i in range(len(tabSpe))}
    affect = {}
    affectations = {i: [] for i in range(len(tabSpe))}

    while spe_libres:  # tant qu'il reste une spe libre
        spe_i = spe_libres.pop()

        while capSpe[spe_i] > 0:  # tant qu'il reste de la capacité et des étudiants à proposer
            etu_j = int(dictSpe[spe_i].pop(0))

            if etu_j not in affect:
                affect[etu_j] = spe_i
                capSpe[spe_i] -= 1
                hq.heappush(affectations[spe_i], (dictEtu[etu_j].index(spe_i), etu_j))
            else:
                curSpe = affect[etu_j]  # spe affectée à l'etu_j
                curIndex = dictEtu[etu_j].index(curSpe)  # index de la spe qui a été affectée à l'etu_j
                index = dictEtu[etu_j].index(spe_i)  # index de la spe_i dans le classement de l'etu_j
                if curIndex > index:  # si la spe_i est mieux classée que la spe affectée
                    spe_libres.append(curSpe)
                    capSpe[curSpe] += 1
                    affect[etu_j] = spe_i
                    capSpe[spe_i] -= 1
                    hq.heappush(affectations[spe_i], (index, etu_j))
                    # Enleve l'etudiantde la specialité actuelle
                    affectations[curSpe] = [(pref, etu) for pref, etu in affectations[curSpe] if etu != etu_j]
                    hq.heapify(affectations[curSpe])

    for spe_h in affectations:
        affectations[spe_h] = [etu for _, etu in sorted(affectations[spe_h])]

    # print(sorted(list(affect.items())))
    return affect    


def testInstable(affectations: dict[int, list[int]], prefEtu: list[list[int]], prefSpe: list[list[int]]):
    pairesInstables = []
    prefEtu = prefEtu.tolist()
    prefSpe = prefSpe.tolist()
    
    for spe, etudiants in affectations.items():
        for etu in etudiants:
            
            idSpe = prefEtu[etu].index(spe) #score de spe dans les prefs de etu
            for speP in prefEtu[etu][:idSpe]: #parcours des spé que etu prefères à la sienne
                
                # il faut que cette spé préfère etu aux siens
                lessPrefSpeP = max([prefSpe[speP].index(i) for i in affectations[speP]])
                for etuP in prefSpe[speP][:lessPrefSpeP]: # on parcours tous les étudiants 
                    
                    if (etuP==etu):
                        pairesInstables.append((spe, etu))
                
# if etuP == etu -> si un des etu de spéPref_deEtu est etu alors instable
    return pairesInstables