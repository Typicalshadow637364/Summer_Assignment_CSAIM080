#Q10	Write a program to Print prime numbers in a range. 
a=int(input("Enter the range:"))
while a>0:
    prime=1
    for i in range(2,a):
        if a%i==0:
            prime=0
    if prime!= 1:
        print(a,"is not Prime")
    else:
        print(a,"is prime")
    a-=1