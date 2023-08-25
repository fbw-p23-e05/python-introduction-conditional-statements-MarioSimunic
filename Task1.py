a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

sum = int(a+b+c)

if a==b==c:
    print("The triple sum is: ", 3*sum)
else:
    print("The sum is: ", sum)