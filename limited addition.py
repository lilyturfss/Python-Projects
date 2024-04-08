# limited addition

num = int(input("Give number : "))
list = []
list.append(num)

while num !=0:
    num = num - 1
    list.append(num)

x= sum(list)
print(x)