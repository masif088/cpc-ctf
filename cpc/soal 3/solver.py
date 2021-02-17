case=int(input())
for j in range (case):
    key=input()
    chiper=input()
    print("case #%i: " %(j+1),end="")
    for i in range (len(chiper)):
        print(chr(ord(key[i%len(key)])+ord(chiper[i])-97) if ord(key[i%len(key)])-97+ord(chiper[i])<=122 else chr(ord(key[i%len(key)])-97+ord(chiper[i])-26),end="")
    print()
