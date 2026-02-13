n,h=map(int,input().split())
arr=list(map(int,input().split()))
count=0

for num in arr:
    if num>h:
        count+=2
    else:
        count+=1    
print(count)
