# a = 1
# print(list(str(a)))
# print

# for i in a:
#     print('caca')
    
a = {}

a["test"] = [1, 3, 2]
a["prout"] = [1, 9]
a["prout"]
for (i, value) in a.items():
    print(i, value)
    
import numpy as np

a = np.empty(dtype=int, shape=(2,2))
a.tolist