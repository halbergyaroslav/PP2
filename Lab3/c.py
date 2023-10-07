list = [int(x) for x in input().split(' ')]
for i in range(1, len(list)): 
    if list[i] > list[i - 1] > 0: print(list[i], end = ' ')
