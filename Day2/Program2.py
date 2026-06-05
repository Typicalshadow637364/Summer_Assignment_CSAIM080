#Q6	Write a program to Reverse a number
#Write a program to find the sum of digits of a no
a= int(input("Enter the no:"))
rev=0
while a>0:
    b=a%10
    a=a//10
    rev=rev*10+b
print("The rev of Number is",rev)