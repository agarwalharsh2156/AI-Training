# dictionary = {
#     "a" : 1,
#     "a" : 2
# }

# print(dictionary)

# ## OUTPUT:
# # {'a': 2}

# import numpy as np
# l = [1,2,3,4]

# a = np.array(l)
# mask = [True, False, True, False]
# print(a[mask])
# print(a[a == 1])
# print(a > 8)
import numpy as np
a = np.array([
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4],
    [1, 2, 4],
])

w = np.array([
    [2],
    [2],
    [2],
    
])

e = np.ones(shape=(3,1))
print(w * e)


b = np.ones(shape=(7,1))
print(b)
r = a@w
print(a@w)
print(a.shape)
print(w.shape)
print(r+b)


