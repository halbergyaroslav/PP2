list = [int(x) for x in input().split(' ')]
my_set = set(list)
ans = 0
for e in my_set: ans += (list.count(e) * (list.count(e) - 1)) // 2 
print(ans)