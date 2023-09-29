list = [int(x) for x in input().split(' ')]
k = int(input())
for i in range(k, len(list) - 1):
    list[i], list[i + 1] = list[i + 1], list[i]
list.pop()
for i in range(len(list)): print(list[i], end = ' ')