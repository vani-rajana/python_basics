#To know weather the given number is even or not using only if-else stmts
while True:
    n=int(input("enter a no: "))
    r=n%2
    #if n==0:
     #   print("progrm end")
     #   break
    if r:
        print("odd")
    else:
        print("even")
    choice =input("do u want to continue? (y/n): ")
    if choice.lower() != "y":
        print("program terminated")
        break