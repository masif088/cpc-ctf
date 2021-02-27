case=int(input())
for i in range(case) :
    a,b,c=input().split(' ')
    a=format(int(a), '02x')
    b=format(int(b), '02x')
    c=format(int(c), '02x')
    print("case #"+str(i+1)+" : " +'#'+a+b+c)
    # print("case #%i: %s" %(i+1,calculate_damage(you,enemy,int(attack),int(defense))))