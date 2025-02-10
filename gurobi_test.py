import tools 
import os

listeEtu = tools.lectureEtu("Ressources/PrefEtu.txt")
speCap = tools.lectureSpe("Ressources/PrefSpe.txt")
listeSpe = speCap[0]
capSpe = speCap[1]

for i in range(3, 10, 1):
    tools.createPLNE(i, listeEtu, capSpe, "Results/PLNE_k"+str(i)+".lp")
    
    command = f"gurobi_cl ResultFile=Results/affects/affectK{i}.sol Results/lp/PLNE_k{i}.lp"
    os.system(command)