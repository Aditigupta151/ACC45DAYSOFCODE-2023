# This year X no of students joined chefs coding classes
X = input("no of students ?")
print(X)

# Y no of chairs are  already present in codeing classes
Y = input("chairs already present ?")
print(Y)

# T is the required chairs
T = int(X) - int(Y)

if T>0 :
   print(str("total chairs required is : ") + str(T))

else :
    print("NO chairs required")


