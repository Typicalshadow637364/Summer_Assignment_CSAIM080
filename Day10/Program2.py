#Write a program to Print reverse pyramid.
#*********
# *******
#  *****
#   ***
#    *
n=int(input("Enter the length of pyramid"))
for i in range(0,n):
    star=2*(n-i) -1
    print(" "*i+"*"*star+" "*i)