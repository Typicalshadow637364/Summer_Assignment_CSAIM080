#Write a program to Print hollow square pattern.
# *****
#*     *
#*     *
#*     *
# *****

n = int(input("Enter the side length: "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")