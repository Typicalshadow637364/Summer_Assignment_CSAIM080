num = int(input("Enter the no:"))
digit=0
while num>0:
    num=num//10
    digit+=1
print ("The no of digit is",digit)