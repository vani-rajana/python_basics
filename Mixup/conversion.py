#find the no of steps to convert x(i/p) to zero if it is odd subtract  -1 , if it is even divide the number by 2.
x=int(input())
step=0
while x!=0:
    if x%2==0:
        x//=2   #x=x//2
    else:
        x=x-1

    step+=1 #step=step+1
print(step)