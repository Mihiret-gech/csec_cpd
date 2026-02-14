for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        r = i         
        c = row.index(1)  
move = abs(r - 2) + abs(c - 2)

print(move)
