import numpy as np


# ANCIEN ALGO
# def galeShapley(tabEtu, tabSpe, cap):
#     capSpe=cap.copy()
#     etuLibre = np.arange(len(tabEtu))
#     speLibre = np.arange(len(tabSpe))
#     tabProp = np.zeros(len(tabEtu), dtype=int)

#     while (len(etuLibre) > 0): #s'il y a du monde, c'est qu'ils nont pas proposé aux spes
#         spe = tabEtu[libre[0]][tabProp[libre[0]]]
#         if (capSpe[spe] > 0):
#             capSpe[spe] -= 1
#         #     speLibre = np.delete(speLibre, np.where(speLibre == spe))
#         #     etuLibre = np.delete(etuLibre, 0)
#         # else:
#         #     for i in range(len(tabSpe[spe])):
#         #         if (tabSpe[spe][i] == etuLibre[0]):
#         #             speLibre = np.append(speLibre, spe)
#         #             etuLibre = np.delete(etuLibre, 0)
#         #             break
        




def galeShapley(tabEtu, tabSpe, cap):
    #   Initialisation
    etu_libres = list(range(len(tabEtu)))
    capSpe = cap.copy() #list[int]    
    dictEtu = {i: list(tabEtu[i]) for i in range(len(tabEtu))} #dict etu - clé: num étu, bucket: liste pref etu (int: int)
    dictSpe = {i: list(tabSpe[i]) for i in range(len(tabSpe))} #dict spe - clé: num spé, bucket: liste pref spé
    affectations = {} #dico résultats, clé: num spé, bucket: liste des étu choisis dans la spé (int, int)

    while (len(etu_libres) != 0):#tant qu'il reste un etu libre
        num_i = etu_libres.pop()            
        spe_h = int(dictEtu[num_i].pop(0)) #premier élément dans les prefs de i (retiré)
        
        if (capSpe[spe_h] > 0): # H n'a pas atteint sa cap max
            capSpe[spe_h] -= 1 #on diminue la capacité restante de H
            if spe_h not in affectations.keys():
                affectations[spe_h] = []
            affectations[spe_h].append(num_i)
        
        else: #on a atteint la capacité max de la spe_H
            max_pref = -1 #(index du moins pref de H)
            worst_etu = None
            for etu in affectations[spe_h]:
                idx_pref = dictSpe[spe_h].index(etu) #indice de l'etu en cours dans les prefs de H
                if (idx_pref > max_pref): #moins pref que celui d'avant
                    max_pref = idx_pref
                    worst_etu = etu #dernier etu affecté dans H, le moins préféré de H
                    
            idx_i = dictSpe[spe_h].index(num_i)
            if (idx_i < max_pref): #h pref I à least_pref
                affectations[spe_h].remove(worst_etu) #supp du pire
                etu_libres.append(worst_etu) #rajout du pire dans les libres
                affectations[spe_h].append(num_i) #ajout du meilleur (i)
                
            else: #H rejette la proposition de i
                etu_libres.append(num_i)
                
    print(sorted(list(affectations.items())))
    return affectations
