#To print the common numbers that are divisible by both 6,9

x=int(input())
y=int(input())
values=[] #divisibe of both 6,9
f1=[] #divisibe of 6
f2=[] #divisibe of 9
for i in range(x,y+1):
    if i%6==0:
        f1.append(i)
    if i%9==0:
        f2.append(i)
    if i%6==0 and i%9==0:
        values.append(i)


print(values)
print(len(values))
print(len(f1))
print(len(f2))
