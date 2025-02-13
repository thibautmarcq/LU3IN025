import tools

import galeshapley as gs

listeEtu = tools.lectureEtu("Ressources/PrefEtu.txt")
speCap = tools.lectureSpe("Ressources/PrefSpe.txt")
listeSpe = speCap[0]
capSpe = speCap[1]

affectEquiEffi = {
    8: [0, 2],
    5: [1],
    6: [3],
    1: [4],
    0: [5, 7],
    7: [6],
    4: [10],
    2: [8],
    3: [9]
}

print(gs.testInstable(affectEquiEffi, listeEtu, listeSpe))
     
   