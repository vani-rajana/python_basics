# Tocheck weather the given number is prime or not using a variable count .

x = int(input("Enter number: "))
count = 0

if x <= 1:   # 0, 1, negative numbers are not prime
    print("np")
else:
    for i in range(1, x + 1):   # check divisibility
        if x % i == 0:
            count += 1

    if count == 2:   # prime has only 2 divisors (1 and itself)
        print("p")
    else:
        print("np")
