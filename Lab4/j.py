n, k = input().split()
n, k = int(n), int(k)

work = set([x for x in range(1, n + 1) if x % 7 not in (6, 0)])
no_work = set(work)

for i in range(k):
    a, b = input().split()
    a, b = int(a), int(b)
    max_no_work = (n - a) // b + 1
    no_work -= {a + b * i for i in range(max_no_work)}
    
print(len(work) - len(no_work))