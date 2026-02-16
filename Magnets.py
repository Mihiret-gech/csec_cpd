n = int(input())
first = input()
groups = 1

for i in range(n - 1):
    second = input()
    if second != first:
        groups += 1
    first = second

print(groups)
