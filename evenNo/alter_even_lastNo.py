# to print the aternative even numbers using 3 parameters of range function
# knowing the last number to stop the loop is logic here
while True:
    x = int(input("enter no:"))
    y = int(input("enter no:"))
    if x % 2 == 0 and y % 2 == 0:
        nums = list(range(x + 2, y, 4))
        for i in range(len(nums)):
            if i == len(nums) - 1:  # last element
                print(nums[i], end=".")
            else:
                print(nums[i], end=",")


    else:
        print("enter only even numbers")

    print()