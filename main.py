a = int(input("Think of a number "))
b = int(input("Think of a number "))
c = int(input("Think of a number "))
if a > b and a > c:
    print("a is the biggest number")
elif b > a and b > c:
    print("b is the biggest number")
elif c > a and c > b:
    print("c is the biggest number")
else:
    print("all the numbers are equal")