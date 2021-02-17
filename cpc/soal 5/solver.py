def chess_board_cell_color(cell1, cell2):
    return (((int(chr(ord(cell1[0])-16))%2==0)==(int(cell1[-1])%2==0))==((int(chr(ord(cell2[0])-16))%2==0)==(int(cell2[-1])%2==0)))
case=int(input())
for i in range (case):
    cell1,cell2=input().split(" ")
    print("case #%i: %s" %(i+1,chess_board_cell_color(cell1,cell2)))
