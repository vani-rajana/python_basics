#To print 1,a,@,1,a,@...series using Variable  symbole to store the elements 1,a,@ in string formate
while True:
    x = int(input("enter a no:"))
    for i in range(1, x + 1):
        '''if i%3==1:
            print("1",end=",")
        elif i%3==2:
            print("a",end=",")
        elif i %3==0:
            print("@",end=",")

         '''

        if i % 3 == 1:
            symbol = "1"
        elif i % 3 == 2:
            symbol = "a"
        elif i % 3 == 0:
            symbol = "@"
        if i == x:
            print(symbol, end=".")
        else:
            print(symbol, end=",")

    print()