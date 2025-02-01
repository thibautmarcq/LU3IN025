import random

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