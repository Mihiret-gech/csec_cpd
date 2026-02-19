s=input()
current="a"
count=0

for character in s:
    d=abs(ord(character)-ord(current))
    count+=min(d,26-d)
    current=character
print(count)    
