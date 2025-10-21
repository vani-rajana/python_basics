a,b=0,1
l=[]
sum=0
count=0
x=int(input())
y=int(input())
while a<=y:
    if a>=x:
        l.append(a)
    c=a+b
    a,b=b,c
print(l)
for i in range(0,len(l),2):
    sum=sum+l[i]
    count=count+1

print(sum/count)