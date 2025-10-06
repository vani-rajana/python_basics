# To swap a pattern after every multiples of 5
# i.e,after 5 multiples fib->bit vice versa
x=int(input("enter no:"))
flag=0
for i in range(1,x+1):
    if i%10==1:
        print(1)
    elif i%5==0:
        print("fitbit")
        if flag:
            flag=0
        else:
            flag=1

    elif i%2==flag:
        print("fit")



    else:
        print("bit")