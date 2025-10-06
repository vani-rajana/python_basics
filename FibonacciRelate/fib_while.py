# fibnoci series using while loop
a=0
b=1
x=int(input())
while a<=x:
    print(a, end=" ")
    c=a+b
    a=b
    b=c