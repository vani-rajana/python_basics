#To print a pattern fit,bit,fit,bit,fitbit,fit,bit....
x=int(input())
for i in range(1,x+1):
    if i%10==1:
        print(1)
    elif i%5==0:
        print("fitbit")
    elif i%2==0:
        print("fit")
    elif i%2!= 0:
        print("bit")