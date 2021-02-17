rule = [0,1,2,
        0,2,3,
        1,3,4,
        2,4,5,
        3,5,6,
        4,6,7,
        5,7,8,
        6,8,9,
        7,9,10
        ]


inp = int(input())

for x in range(inp):
    st = input()
    for x in range(len(st)):
        if(ord(st[x]) < 97 or ord(st[x]) > 122):
            print(chr(ord(st[x])),end="")
        else:
            if((ord(st[x])+(rule[x])) > 122):
                print(chr((ord(st[x])-26+(rule[x]))),end="")
                
            else:
                print(chr(ord(st[x])+(rule[x])),end="")
