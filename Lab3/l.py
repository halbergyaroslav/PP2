list = [int(x) for x in input().split(' ')]
k, c = input().split(' ')
k, c = int(k), int(c)
list.append(c)
for i in range(len(list) - 1, k, -1):
    list[i], list[i - 1] = list[i - 1], list[i]
for i in range(len(list)): print(list[i], end = ' ')