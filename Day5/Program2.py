#	Write a program to Check strong number.	
def fact(a):
    b=1
    while a>0:
        b=b*a
        a-=1
    return b
sum=0
n=int(input("Enter the number:"))
a=n
while n>0:
    b=n%10
    n=n//10
    sum+= fact(b)
if sum==a:
    print("It's a strong no")
else:
    print("It's not a strong no")
    