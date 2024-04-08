# problem 8
a = [1,2,3,4,5,6,7,7,8,9,10]
v = set()
duplicados = []

for x in a:
    if x in v:
        duplicados.append(x)
    else:
        v.add(x)
print(duplicados)
