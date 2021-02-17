banyak = int(input())
nilai = []
temp1 = bool(True)
temp2 = bool(True)
for i in range(banyak):
    posisi = input().split()
    scores = list(map(str, posisi))
    
    if (int(scores[0][1]) % 2 == 1 and (scores[0][0] == 'A' or scores[0][0] == 'C' or scores[0][0] == 'E' or scores[0][0] == 'G') ) or  (int(scores[0][1]) % 2 == 0 and (scores[0][0] == 'B' or scores[0][0] == 'D' or scores[0][0] == 'F' or scores[0][0] == 'H')) :
        temp1 = True
    else:
        temp1 = False
        
    if (int(scores[1][1]) % 2 == 1 and (scores[1][0] == 'A' or scores[1][0] == 'C' or scores[1][0] == 'E' or scores[1][0] == 'G') )  or (int(scores[1][1]) % 2 == 0 and (scores[1][0] == 'B' or scores[1][0] == 'D' or scores[1][0] == 'F' or scores[1][0] == 'H')) :
        temp2 = True
    else:
        temp2 = False
    
    if temp1 == temp2:
        nilai.append(True)
    else:
        nilai.append(False)
        
for i in range(banyak):
    print(nilai[i], end='')
    print()
