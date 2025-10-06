#Fibonacci series using for loop
a=0
b=1
x=int(input())
for i in range(1000):
    if a>x:
        break

    else:
        print(a,end=" ")
        c=a+b
        a=b
        b=c