def thirt(n):
    cpn=n
    div=0
    loop=True
    diver=[1,10,9,12,3,4]
    a=0
    while(loop):
        rev=str(cpn)[::-1]
        div=0
        for i in range(len(rev)):
            div+=(int(rev[i])*diver[i%6])
        cpn=div
        if div%13==n%13 and len(str(div))==2:
            return div
case=int(input())
for i in range(case):
    print("case #%i: %i" %((i+1),thirt(int(input()))))
