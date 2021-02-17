import string
import random
from random import randrange
print(100)
for i in range(100):
    all_chars = list(string.digits)
    random.shuffle(all_chars)
    b= (''.join(all_chars[:94])[int(randrange(10))::])

    a=[["."]*11]*11
    c=1
    con=0
    for i in range(len(b)):
        if c==1:
            for j in range(11):
                a[j][con]=b[i]
            c=0
        elif c==0:
            a[con]=[b[i]]*11
            c=1
        con+=1
    for i in range (len(a)):
        for j in range(len(a[i])):
            print(a[i][j],end="")
        print()
