dictionary = {
    "a" : 1,
    "a" : 2
}

print(dictionary)

## OUTPUT:
# {'a': 2}

import numpy as np
l = [1,2,3,4]

a = np.array(l)
mask = [True, False, True, False]
print(a[mask])
print(a[a == 1])
print(a > 8)

