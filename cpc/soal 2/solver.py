import math
def bomber():
    lv=int(input())
    p=int(input())
    tembok=[]
    for i in range(p):
        tembok.append(sorted(input()))
    ret=0
    a=1
    for i in range(p):
        ret+=(math.floor(math.ceil(int(tembok[i][0])/lv)/3)+math.ceil(int(tembok[i][0])/lv))
    return ret
case = int(input())
for i in range(case):
    print("case #%i: %i" %((i+1),bomber()))
