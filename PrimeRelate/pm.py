
def is_prime(n):
    count=0
    for i in range(2,n,1):
        if n%i==0:
            count=count+1
    if count==0:
        return True
    else:
        return False
l=[]
l1=[]
sum=0
x=int(input())
y=int(input())
for i in range(x,y):
    res=is_prime(i)
    if res == True:
        l.append(i)
        sum=sum+i
print(sum/len(l))

for i in range(1,len(l),2):
        l1.append(l[i])
print(l1)