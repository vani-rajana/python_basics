# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

x = int(input())
size = list(map(int, input().split()))
size_count = Counter(size)
cus = int(input())
total = 0

for _ in range(cus):
    s, cost = map(int, input().split())
    if s in size_count and size_count[s] > 0:   # check if size exists and is in stock
        size_count[s] -= 1   
        total += cost
    else:
        print(f"Size {s} not available, skipping this order")

print(total)
