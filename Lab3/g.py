list = [int(x) for x in input().split(' ')]
y = int(input())
c = 0
list.sort(reverse = True)
for i in range(len(list)):
    if list[i] < y:
        print(i + 1)
        c = 1
        break
if not c: print(len(list) + 1)