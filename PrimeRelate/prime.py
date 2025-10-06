# To check weather the give number is prime or not

x = int(input("Enter number: "))

if x <= 1:   # 0,1, negative numbers are not prime
    print("np")
else:
    for i in range(2, x):
        if x % i == 0:   # if divisible by something other than 1 and itself
            print("np")
            break
    else:
        print("p")

