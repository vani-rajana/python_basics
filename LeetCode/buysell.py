# best time to sell and buy stock : leet code problem
l=[8,2,4,9,6,1]
p=-20
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]-l[i]>p:
            p=l[j]-l[i]


    if p>op:
        op=p

print(op)