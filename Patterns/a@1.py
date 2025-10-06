# To print the pattern 1,a,@,1,a,@.....
while True:
    x=int(input())
    for i in range(x-1):
        if i%3==0:
            print("1",end=",")
        elif i %3==1:
            print("a", end =" ,")
        elif i%3==2:
            print("@", end =" ,")

    if (x-1)%3==0:
        print(1,end=".")
    elif(x-1)%3==1:
        print('a',end=".")
    else:
        print('@',end=".")

    print()