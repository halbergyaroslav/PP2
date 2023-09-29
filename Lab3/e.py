list = [int(x) for x in input().split(' ')]
c = 0
for i in range(1, len(list) - 1): 
    if list[i] - list[i - 1] > 0 and list[i] - list[i + 1] > 0: c += 1
print(c)
