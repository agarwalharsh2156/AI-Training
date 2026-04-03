l = [1,2,3,4,5,6,6,7,7,8,8]
s = set(l)

print(l)
print(s)

even = list(filter(lambda x: x%2 == 0, l))
print(even)


string = "10 30 40 50"
mapd = list(map(int, string.split(" ")))
print(mapd)


rev = sorted(l, reverse=True)
print(rev)

l.sort(reverse= True)
print(l)

names = ["Harsh", "Hbrsh", "Krisha", "Aditi"]
sorted_names = sorted(names, key = lambda x: x[1])
print(sorted_names)