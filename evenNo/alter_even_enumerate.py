# to print alternative even numbers using enumerate method
while True:
    x=int(input("enter no:"))
    y=int(input("enter no:"))
    if x%2==0 and y%2==0:
        for idx, i in enumerate(range(x + 2, y, 4)):
            if idx == 0:
                print(i, end="")  # first number (no comma before)
            else:
                print(",", i, sep="", end="")  # comma before other numbers
        print(".")

    else:
        print("enter only even numbers")

    print()