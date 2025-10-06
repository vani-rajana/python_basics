# To print corresponding alphabet to the fibnoci series
a=0
b=1
x=int(input())

while a<x:
    #print(a,end=" ")
    print(chr(96+a),end=" ")
    c=a+b
    a=b
    b=c