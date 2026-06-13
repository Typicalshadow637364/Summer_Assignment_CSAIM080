#Write a program to Write function to check prime
def prime(a):
    prime= 1
    for i in range(2,a):
        if a%i==0:
            prime=0
    if prime!= 1:
        print("It's not Prime")
    else:
        print("It's prime")
n=int(input("Enter the number"))
prime(n)