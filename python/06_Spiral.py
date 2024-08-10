import sys
limit = int(input())

for _ in range(limit):
    row, col= map(int, sys.stdin.readline().split())
    
    if row >= col:
        if row % 2 == 0:
            res = row**2 - col +1
        else:
            res= (row-1)**2 + col
    else:
        if col % 2 == 1:
            res = col**2 - row +1
        else:
            res = (col-1)**2 + row 
    print(res)