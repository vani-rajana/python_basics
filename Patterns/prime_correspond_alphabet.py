# To print the alphabets corresponding to prime numbers
def isprime(x):
    for i in range(2,x):
        if x%i==0:
            return False


    else:
        return  True

for i in range(2,27):
    if isprime(i):
        print(chr(96+i))
