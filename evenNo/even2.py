# To check weather the given number is even or not using multiple for loops
while True:
    x= int(input("enter ano: "))
    if x%2==0:
        for i in range(1,x):
            if i==x-2:
                print(i,end=".")
            elif i%2==0:
                print(i,end=" ,")
    else:
        for i in range(1,x):
            if i== x-1:
                print(i,end=".")
            elif i%2==0:
                print(i,end=",")
    print()