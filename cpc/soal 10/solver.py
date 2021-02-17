def bouncingBall():
    h, bounce, window=input().split(" ")
    h=int(h)
    bounce=float(bounce)
    window=int(window)
    if (0<h>window and 0 < bounce < 1)==False:
        return -1
    b=1
    while(True):
        h*=bounce
        if(h<=window):
            return b
        else:
            b+=2
    return b
case =int(input())
for i in range(case):
    print("case #%i: %i" %((i+1),bouncingBall()))
