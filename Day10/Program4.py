#Write a program to Print character pyramid.
#    A
#   ABA
#  ABCBA
# ABCDCBA
#ABCDEDCBA
n=int(input("Enter the length of pyramid"))
for i in range(1,n+1):
    space=n-i
    print(" "*space,end="")
    s=1
    while s<i:
        print(chr(s+64),end="")
        s+=1
    while s>0:
        print(chr(s+64),end="")
        s-=1
    print(" "*space)