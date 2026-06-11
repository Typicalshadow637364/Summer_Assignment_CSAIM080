#Write a program to Print number pyramid.
#    1
#   121
#  12321
# 1234321
#123454321
n=int(input("Enter the length of pyramid"))
for i in range(1,n+1):
    space=n-i
    print(" "*space,end="")
    s=1
    while s<i:
        print(s,end="")
        s+=1
    while s>0:
        print(s,end="")
        s-=1
    print(" "*space)