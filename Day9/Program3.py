#Write a program to Print repeated character pattern.
#A
#BB
#CCC
#DDDD
#EEEEE
n=int(input("Enter the length of pyramid"))
a=""
b=65
for i in range(1,n+1):
     print(chr(b)*i)
     b+=1