#	Write a program to Check perfect number.	
n= int(input("Enter the number:"))
a=0
for i in range (1,n):
    if n%i==0:
        a+=i
if a==n:
    print("It's a Perfect Number")
else:
    print("It's not a Perfect Number")
    