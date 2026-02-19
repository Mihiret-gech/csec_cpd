cal=list(map(int,input().split()))
str=input()
total=0

for character in str:
    if character=="1":
        total+=cal[0]
    elif character=="2":
        total+=cal[1]
    elif character=="3":
        total+=cal[2]
    elif character=="4":
        total+=cal[3]   
print(total)         

