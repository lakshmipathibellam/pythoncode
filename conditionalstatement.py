n1=int(input("enter a number :"))
n2=int(input("enter a number :"))
n3=int(input("enter a number :"))

if n1>n2 and n1>n3:
    print("the big number is:",n1)
elif n2>n3:
    print("the big number is:",n2)
else:
    print('the big number is:',n3)