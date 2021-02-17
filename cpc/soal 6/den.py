import math

effectiveness = {

"electric":{

"electric": 0.5,

"fire": 1,

"grass": 1,

"water": 2,

"stell":2

},

"fire":{

"electric": 1,

"fire": 0.5,

"grass": 2,

"water": 0.5,

"stell":2

},

"grass":{

"electric": 1,

"fire": 0.5,

"grass": 0.5,

"water": 2,

"stell":0.5

},

"water":{

"electric": 0.5,

"fire": 2,

"grass": 0.5,

"water": 0.5,

"stell":2

},

"stell":{

"electric": 0.5,

"fire": 0.5,

"grass": 2,

"water": 0.5,

"stell":0.5

}
}

inp = int(input())

for x in range(inp):
    a,b,c,d = input().split(" ")
    hasil = 50 * (float(c) / float(d)) * effectiveness[a][b]
    print("case #{0}: {1}".format(x+1, math.floor(hasil)+1))
