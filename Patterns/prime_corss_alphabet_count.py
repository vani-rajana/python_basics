# Prime numbers between 1 and 26 with alphabets using count

for i in range(1, 27):   # numbers from 1 to 26
    count = 0
    for j in range(1, i + 1):   # check divisors
        if i % j == 0:
            count += 1
    if count == 2:   # prime numbers have exactly 2 divisors
        print(i, "=", chr(96 + i))