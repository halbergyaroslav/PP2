list = input().split(' ')
my_set = set()

for e in list:
    if e in my_set: print("YES")
    else: 
        print("NO")
        my_set.add(e)