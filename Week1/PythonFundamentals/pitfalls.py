def func(a = 0, L = []):
    a += 1
    L.append(L)
    
    # L.append(a)
    print(L)

# func()
func(L = [2,3,4])
# func()
# func()
# func()
#######################################################

L = [1]
L.append([])
print(L)

#######################################################

def func(l = []):
    print(l)
    print(id(l))
    return l

#######################################################

b = [1,2,3]
c = func(b)
print(id(b))
print( b is c)

l1 = [1,2]
l2 = [1,2]
print(id(l1), "---", id(l2))
print(l1 is l2)

#######################################################

def func(l = []):
    l.append(1)
    l.append(2)
    return l

b = [5,6]
l = func(b)
print(b)
print(l)
print(b is l)
print(id(b), "---", id(l))


