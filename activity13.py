

a = eval(input("Enter a number: "))
c = 1
for b in range (a, 0, -1):
    c *= b
    print (f"The factorial of {a} is {c}")