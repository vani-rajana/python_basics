#alterntive even numbers used join to get desired output
while True:
    x=int(input("enter lower range no:"))
    y=int(input("enter upper range number:"))
    if x%2==0 and y%2==0:
        res=[]
        for i in range(x+1,y):
            if i==y-2:
                res.append(i)
            elif i %2==0:
                res.append(i)
        print(",".join(map(str, res[::2])))
        # print(",".join(map(str, res[::2])) + ".")
    else:
        print("enter only even numbers")

    print()