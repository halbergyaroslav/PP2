list = [int(x) for x in input().split(' ')]
for i in range(1, len(list), 2):
    list[i], list[i - 1] = list[i - 1], list[i]
for i in range(len(list)): print(list[i], end = ' ')
