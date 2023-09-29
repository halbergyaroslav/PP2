n, k = input().split(' ')
n, k = int(n), int(k)

list = ['I' for x in range(n)]
for i in range(k):
    l, r = input().split(' ')
    l, r = int(l), int(r)
    for e in range(l - 1, r, 1): list[e] = '.'
for i in range(len(list)): print(list[i], end = '')