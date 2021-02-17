import collections
def the_order_of():
    horizontal=[]
    
    for i in range(11):
        horizontal.append(input())
    vertikal= [(horizontal[j][i]) for i in range(11) for j in range (11)]
    vertikal =[vertikal[i:i+11] for i in range(0, len(vertikal), 11)]
    horizontal=[collections.Counter(i).most_common(1)[0] for i in horizontal if collections.Counter(i).most_common(1)[0][0] != "." ]
    vertikal=[collections.Counter(i).most_common(1)[0] for i in vertikal if collections.Counter(i).most_common(1)[0][0] != "." ]
    horizontal=sorted(horizontal, key = lambda x: x[1],reverse=True)
    vertikal=sorted(vertikal, key = lambda x: x[1],reverse=True)
    look=False
    first=0
    if len(horizontal)>0:
        first= 1 if horizontal[0][1]==11 else 0
    value=""
    h=0
    v=0
    for i in range(len(horizontal)+len(vertikal)):

        if first==1:
            value+=horizontal[h][0]
            h+=1
            first=0
        else:
            value+=vertikal[v][0]
            v+=1
            first=1
    return value[::-1]
case=int(input())
for i in range(case):
    print("case #%i: %s" %((i+1),the_order_of()))
# print(())
