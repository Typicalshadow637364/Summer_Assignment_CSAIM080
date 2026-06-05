#Q8	Write a program to Check whether a number is palindrome.
a= int(input("Enter the no:"))
rev=0
c=a
while a>0:
    b=a%10
    a=a//10
    rev=rev*10+b
if rev==c:
    print("The Number is Palindrome")
else:
    print("The Number is not Palindrome")