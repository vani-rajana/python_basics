# To print alternative fibnoci series
a=int(input())
b=int(input())
s=[]
for i in range(a,b):
    for j in range(1,i):
        s.append(j)
    c=a+b
    a=b
    b=c
print(s)