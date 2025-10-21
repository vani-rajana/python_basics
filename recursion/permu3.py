l=[]
def permu(s,res=""):
    global l
    if len(s)==0:
        l.append(res)

    for i in range(len(s)):
        ns=s[i]+s[i+1:]
        ch=s[i]
        permu(ns,res+ch)

    return l
print(permu("abc"))