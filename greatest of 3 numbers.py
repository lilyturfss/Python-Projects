#greatest of 2 numbers/3 numbers

numone=  int(input("give me a number: "))
numtwo= int(input("give me another number: "))
numthree= int(input("give me another number x2: "))

if numone>numtwo and numone>numthree:
    print("the first one is bigger")
elif numtwo>numone and numtwo>numthree:
    print("the second one is bigger")
elif numthree>numtwo and numthree>numone:
    print("the third one is bigger")
else:
    print("they are all literally the same number")
