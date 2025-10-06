#To count the frequency of each element in a list without using the count() method.
l=[1,1,2,3,1,2,3,4,1]
d={ }
for i in l:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for k,v in d.items():           #l.count ki replacement method
    print(f'{k} is repeated {v} times')

