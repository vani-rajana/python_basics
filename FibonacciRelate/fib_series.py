#To print fibnoci series
a=0
b=1
c=0
x=int(input("enter the range: "))
print(a,b,end=" ")
for i in range(x):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

