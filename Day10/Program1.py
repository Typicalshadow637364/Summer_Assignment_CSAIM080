#Write a program to Print star pyramid.
#    *
#   ***
#  *****
# *******
#*********
n=int(input("Enter the length of pyramid"))
for i in range(1,n+1):
    star=2*i-1
    space=n-i
    print(" "*space+"*"*star+" "*space)