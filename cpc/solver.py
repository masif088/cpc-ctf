def keygen():
    plain="ABCDEFGHIJKLMNOPQRSTQUVWXYZ"
    key=input("input kunci :").upper()
    key=removeDupWithOrder(key)
    for i in plain:
        for j in range(len(key)):
            if key[j]==i:
                break
            if j==len(key)-1:
                key+=i
    return key
jumlahkunci=int(input("jumlah kunci : "))
kunci=[None]*jumlahkunci
for i in range (jumlahkunci):
    kunci[i]=keygen()
plain="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cek=input("input plain text : ").upper()
hasil=""
for i in range(len(cek)):
    c=i%len(kunci)
    key=kunci[c]
    hasil+=key[plain.index(cek[i])]
print(hasil)
