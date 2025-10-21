
def permu(s,res=""):
    if len(s)==0:
        print(res)
        return
    for i in range(len(s)):
        ns=s[i]+s[i+1:]
        ch=s[i]
       permu(ns,res+ch)


print(permu("abc"))