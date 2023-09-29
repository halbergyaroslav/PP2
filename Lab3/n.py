list = [int(x) for x in input().split(' ')]
for e in list:
    if list.count(e) == 1: print(e, end = ' ')