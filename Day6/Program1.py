#Write a program to Convert decimal to binary.
n=int(input("Enter the decimal number:"))
b=""
while n>1:
    a=n%2
    b=str(a)+b
    n=n//2
b=str(1)+b
print("The binary number is:",b)

