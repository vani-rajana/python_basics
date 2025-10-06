# To print 1,a,@,1,a,@....using list method called APPEND
while True:
    x=int(input("enter a no:"))
    res=[]
    for i in range(1,x+1):
        if i%3==1:
            res.append("1")
        elif i%3==2:
            res.append("a")
        elif i%3==0:
            res.append("@")
    print(res)
    print(",".join(res))
