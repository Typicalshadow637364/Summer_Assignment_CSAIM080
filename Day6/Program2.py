#Write a program to Convert binary to decimal.
n=int(input("Enter the binary number"))
i=0
b=0
while n>0:
    a=n%10
    n=n//10
    b=b+(a*(2**i))
    i+=1
print("The decimal number is",b) 