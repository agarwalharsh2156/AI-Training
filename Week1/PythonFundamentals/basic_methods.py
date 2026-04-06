l = [1,2,3,4,5,6,6,7,7,8,8]
s = set(l)

print(l)
print(s)

# filter verifies for each element from the passed data structure if it satisfies the function, 
# if True, keeps it in the object data structure, else ignores it.
even = list(filter(lambda x: x%2 == 0, l))
print(even)

# applies the argument function to each and every element of the given data structure.
string = "10 30 40 50"
mapd = list(map(int, string.split(" ")))
print(mapd)

# returns a new datastructure a sorted version of the argumented data strucutre.
rev = sorted(l, reverse=True)
print(rev)

# makes changes to the datastructure itself which is irreversible.
l.sort(reverse= True)
print(l)

# using key for custom key based sorting on a data structure which is not in-place sorting like .sort()
names = ["Harsh", "Hbrsh", "Krisha", "Aditi"]
sorted_names = sorted(names, key = lambda x: x[1])
print(sorted_names)

# zip two different datastructures together for querying them together.

# 