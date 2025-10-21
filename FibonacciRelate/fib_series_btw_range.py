a,b=0,1
x=int(input())
y=int(input())
l1=[]
sum=0
while a<=y:
    c=a+b
    if x<=a<=y:
        l1.append(a)
    a=b
    b=c
for i in range(0,len(l1),1):
    sum=sum+l1[i]
print(sum/len(l1))