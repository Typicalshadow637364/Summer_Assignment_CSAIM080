#Write a program to find the sum of digits of a no
a= int(input("Enter the no:"))
sum=0
while a>0:
    b=a%10
    a=a//10
    sum+=b
print("The sum of digits is",sum)
