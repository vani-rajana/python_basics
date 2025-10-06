'''weatther the problem can become 100 or not
check x<100
even +5
odd *2
can x be 100 or not''''''
'''
x = int(input("Enter a number: "))

while x < 100:
    if x % 2 == 0:   # even
        x += 5
    else:            # odd
        x *= 2
    print("Current value:", x)

if x == 100:
    print("Yes, it became 100.")
else:
    print("No, it cannot be exactly 100. Final value:", x)
