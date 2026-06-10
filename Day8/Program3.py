#Write a program to Print character triangle.
#A
#AB
#ABC
#ABCD
#ABCDE
n=int(input("Enter the length of pyramid"))
a=""
b=65
for i in range(1,n+1):
     a=a+chr(b)
     print(a)
     b+=1