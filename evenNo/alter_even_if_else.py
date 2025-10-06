#  To print alternative even numbers only using if-else stmts
while True:
    x = int(input("Enter lower even number: "))
    y = int(input("Enter upper even number: "))

    # exit condition (optional)
    if x == 0 or y == 0:
        print("Exiting program...")
        break

    # check if both numbers are even
    if x % 2 == 0 and y % 2 == 0:
        # generate even numbers between x and y in steps of 4
        res = list(range(x + 2, y, 4))

        if res:  # if list is not empty
            print(",".join(map(str, res)) + ".")
        else:
            print("No even numbers in this range.")
    else:
        print("Please enter only even numbers.")
