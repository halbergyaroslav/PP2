n = int(input())

my_set = set()

for e in range(n):
    for e in input().split(' '): my_set.add(e)
    
print(len(my_set))