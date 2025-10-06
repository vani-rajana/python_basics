# To know weather the given number is even or not
while True:
    x= int(input("enter a no: "))
    for i in range(1,x):
        if x%2==0:
            if i ==x-2:
                print(i,end=".")
            elif i%2==0:
                print(i, end=" ,")
        else:
            if i == x-1:
                print(i,end=".")
            elif i%2==0:
                print(i,end=",")
    print()