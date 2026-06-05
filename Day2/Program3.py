#Q7	Write a program to Find product of digits
a= int(input("Enter the no:"))
pro=1
while a>0:
    b=a%10
    a=a//10
    pro=pro*b
print("The Product of digits is",pro)