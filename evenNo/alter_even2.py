#print alternative even numbers using if-else and for loop
while True:
    a=int(input("enter a :"))
    b=int(input("enter b: "))
    c=0
    for i in range(a+1,b):
        if i %2==0:
            if c%2==0:
                print(i,end=" ")

            c+=1  #c=c+1
    print()