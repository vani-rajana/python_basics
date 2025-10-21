# To print alternative fibnoci series
n=int(input())
a,b=0,1
l=[0,1]
count=0
sum=0
for i in range(2,n):
    c=a+b
    l.append(c)
    a,b=b,c
print(l)
for i in range(0,len(l),2):
    print(l[i],end=" ")
    sum=sum+l[i]
    count=count+1
print()
print(sum/count)

