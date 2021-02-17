def finance(n):
    n+=1
    a=0
    b=n
    sn=0
    c=0
    for i in range(b):
        c=(n/2)*(2*a+(n-1)*1)
        sn+=c
        n-=1
        a+=2
    return sn
case=int(input())
for i in range(case):
    print("case #%i: %i" %((i+1),finance(int(input()))))
