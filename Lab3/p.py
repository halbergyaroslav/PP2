list_x = []
list_y = []
for i in range(8):
    x, y = input().split(' ')
    x, y = int(x), int(y)
    list_x.append(x)
    list_y.append(y)
c = 1
for i in range(8):
    for j in range(i + 1, 8):
        if list_x[i] == list_x[j] or list_y[i] == list_y[j] or abs(list_x[i] - list_x[j]) == abs(list_y[i] - list_y[j]): c = 0
if c: print('NO')
else: print('YES')