x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

c = 0

if abs(x1 - x2) == abs(y1 - y2): c = 1
if x1 == x2 or y1 == y2: c = 1

if c: print("YES")
else: print("NO")