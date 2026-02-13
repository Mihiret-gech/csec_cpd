n = int(input())
s = input()
 
A = 0
D = 0
 
for letter in s:
    if letter == "A":
        A += 1
    else:
        D += 1
 
if A > D:
    print("Anton")
elif A < D:
    print("Danik")
else:
    print("Friendship")
