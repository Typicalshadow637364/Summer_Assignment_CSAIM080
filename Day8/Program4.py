#Write a program to Print repeated-number pattern.
#1
#22
#333
#4444
#55555
n=int(input("Enter the length of pyramid"))
for i in range(0,n+1):
    print(str(i)*i)