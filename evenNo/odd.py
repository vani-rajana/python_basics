#To print the odd numbers in the given range
while True:
    x=int(input("en no: "))
    for i in range(1,x):
        if x%2==0:
            if i == x-1:
                print(i,end=" .")

            elif i%2 != 0:
                print(i,end=" ,")

        else:
            if i== x-2:
                print(i,end="." )
            elif i%2!= 0:
                print(i,end=",")