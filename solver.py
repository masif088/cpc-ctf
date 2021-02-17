a=int(input())
gan=0
gen=0
count=0
for i in range(1,a):
    count+=i
    if i%2==0:
        gen+=1
    else:
        gan+=1
print("jumlah bilangan genap: %i"%(gen))
print("jumlah bilangan ganjil: %i"%(gan))
print("total penjumlahan semua bilangan: %i"%(count))
