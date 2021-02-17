def decoder():
    encoded=input()
    marker=input()
    n=len(marker)
    a=""
    b=""
    c=""
    rev=False
    i=0
    while(i<len(encoded)):
    # for i in range():
        if encoded[i:i+n:] == marker:
            if rev==False:
                rev=True
            else:
                rev=False
            i+=n
        elif rev:
            b+=encoded[i]
            i+=1
        else:
            a+=encoded[i]
            i+=1
    return(a+b[::-1])
case=int(input())
for i in range(case):
    print("case #%i: %s" %((i+1),decoder()))
