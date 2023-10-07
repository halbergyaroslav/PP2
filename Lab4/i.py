n = int(input())
list = []

for i in range(n):
    k = int(input())
    my_set = set()
    for j in range(k): my_set.add(input())
    list.append(my_set)

total, common = list[0], list[0]

for e in list:
    total = total.union(e)
    common = common.intersection(e)

print(len(common))
print('\n'.join(sorted(common)))

print(len(total))
print('\n'.join(sorted(total)))