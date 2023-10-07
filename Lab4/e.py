n, m = input().split(' ')
n, m = int(n), int(m)

anya = set()
borya = set()

for i in range(n):
    anya.add(int(input()))

for i in range(m):
    borya.add(int(input()))

print(len(anya.intersection(borya)))
print(' '.join(str(x) for x in sorted(anya.intersection(borya))))

print(len(anya.difference(borya)))
print(' '.join(str(x) for x in sorted(anya.difference(borya))))

print(len(borya.difference(anya)))
print(' '.join(str(x) for x in sorted(borya.difference(anya))))