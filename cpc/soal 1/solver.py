def faktorisasiprima(i):
    x=int(input())
    factorlist=""
    count=0
    loop=2

    looper=True
    while looper:
        if x%loop==0:
            x/=loop
            count+=1
        else:
            if count>1:
                factorlist+=("%i^%i*"%(loop,count))
            elif count==1:
                factorlist+=("%i*"%(loop))
            count=0

            loop+=1
        looper=loop<=x
        if looper==False:
            if count>1:
                factorlist+=("%i^%i"%(loop,count))
            elif count==1:
                factorlist+=("%i"%(loop))
    print("case #%i: %s"%(i+1,factorlist))
for i in range(int(input())):
    faktorisasiprima(i)
