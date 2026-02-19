n=int(input())
s=list(map(int,input().split()))
police=0
untreated=0

for crimes in s:
    if crimes==-1:
        if police>0:
            police-=1
        else:
            untreated+=1
    else:
        police+=crimes

print(untreated)




    
