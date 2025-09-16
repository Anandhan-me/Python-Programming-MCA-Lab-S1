b1=int(input("Enter the first number : "))
b2=int(input("Enter the second number : "))
b3=int(input("Enter the third number : "))
if b1>b2 and b1>b3 :
    print(b1," is greater than ",b2," and ",b3)
elif b2>b3 :
    print(b2," is greater than ",b1," and ",b3)
else :
    print(b3," is greater than ",b1," and ",b2)