def encryp():
    count=1
    count3=0
    char=input()
    real=char[0]
    for i in range(1,len(char)):
        if i%3==0:
            if ord(char[i])==32:
                real+=char[i]
            else:
                real+=chr(ord(char[i])+count3) if (ord(char[i])+count3)<26+97 else chr(ord(char[i])+count3-26)
            count3+=1
            count-=1
        else:
            if ord(char[i])==32:
                real+=char[i]
            else:
                real+=chr(ord(char[i])+count) if (ord(char[i])+count)<26+97 else chr(ord(char[i])+count-26)
            count+=1
    return(real)
case =int(input())
for i in range(case):
    print("case #%i: %s" %((i+1),encryp()))
