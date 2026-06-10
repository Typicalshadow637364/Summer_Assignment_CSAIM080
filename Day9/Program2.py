#Write a program to Print reverse number triangle.

#12345
#1234
#123
#12
#1
n=int(input("Enter the length of pyramid:"))
while n > 0:
    for i in range(1, n + 1):
        print(i, end="")
    print()
    n -= 1