import numpy as np

def galeShapley(tabEtu, tabSpe, cap):
    capSpe=cap.copy()
    etuLibre = np.arange(len(tabEtu))
    speLibre = np.arange(len(tabSpe))
    tabProp = np.zeros(len(tabEtu), dtype=int)

    while (len(etuLibre) > 0): #s'il y a du monde, c'est qu'ils nont pas proposé aux spes
        spe = tabEtu[libre[0]][tabProp[libre[0]]]
        if (capSpe[spe] > 0):
            capSpe[spe] -= 1
        #     speLibre = np.delete(speLibre, np.where(speLibre == spe))
        #     etuLibre = np.delete(etuLibre, 0)
        # else:
        #     for i in range(len(tabSpe[spe])):
        #         if (tabSpe[spe][i] == etuLibre[0]):
        #             speLibre = np.append(speLibre, spe)
        #             etuLibre = np.delete(etuLibre, 0)
        #             break
