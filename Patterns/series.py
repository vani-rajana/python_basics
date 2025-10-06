#print 1,2,4,7,11,16,22,29....series till x(i/p)
n = int(input("Enter number of terms: "))

num = 1
diff = 1
for _ in range(n):
    print(num, end=" ")
    num += diff
    diff += 1
