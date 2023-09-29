list = [int(x) for x in input().split(' ')]
for i in range(len(list)): 
    if list[i] % 2 == 0: print(list[i], end = ' ')