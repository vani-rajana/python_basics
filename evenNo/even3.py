while True:
    x=int(input("enter a no:"))
    l=0
    if x%2==0:
        l=x-2
    else:
        l=x-1
    for i in range(1,x):
        if i==l:
            print(i,end=".")
        elif i %2==0:
            print(i,end=",")
    print()