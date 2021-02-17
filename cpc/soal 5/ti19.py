huruf = ['B','D','F','H']
huruf1 = ['A','C','E','G']
nomor = ['1','3','5','7']
nomor1 = ['2','4','6','8']
pemisah = []
jumlahCase = int(input())
for i in range(jumlahCase):
    isi = input()
    pemisah.append(isi)


for a in pemisah:
    if ((a[0] in huruf and a[4] in huruf) and (a[1] in nomor and a[5] in nomor)) or ((a[0] in huruf1 and a[4] in huruf1) and (a[1] in nomor and a[5] in nomor)) or ((a[0] in huruf and a[4] in huruf) and (a[1] in nomor1 and a[5] in nomor1)) or ((a[0] in huruf1 and a[4] in huruf1) and (a[1] in nomor1 and a[5] in nomor1)):
        print("Case #{} : True" .format(pemisah.index(a) + 1))
    else:
        print("Case #{} : False" .format(pemisah.index(a) + 1))
