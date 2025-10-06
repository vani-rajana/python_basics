# To print alternative prime numbers

x=int(input())
y=int(input())
s=[]
for i in range(x,y):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        s.append(i)
        #print(i, end=" ")  # if the number is prime it added to list
#print(s)  # s contain all the primes between the range x,y
#print(s[::2]) to get alternative primes from list
print(",".join(map(str, s[::2])) ) # join remove the unwanted parantesis

