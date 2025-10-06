# To print alternative even numbers
while True:
    x = int(input("enter no:"))
    y = int(input("enter no:"))

    if x % 2 == 0 and y % 2 == 0:

        for i in range(x + 2, y, 4):  # without including start value

            print(i, end=",")
        print(".")

        '''

         for i in range(x+1,y):
            if i==y-2:
                print(i)
            elif i%2==0:
                print(i,end=",")
        '''


    else:
        print("enter only even numbers")

    print()