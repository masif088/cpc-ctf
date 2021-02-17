from collections import OrderedDict
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))
def next_happy_year(year):
    looper=True
    while (looper):
        year+=1
        if (len(str(year))==len(removeDupWithOrder(str(year)))):
            looper=False
    return year
case=int(input())
for i in range(case):
    print("case #%i: %s" %(i+1,next_happy_year(int(input()))))
