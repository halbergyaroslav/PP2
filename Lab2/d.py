year = int(input())

if year % 4 != 0: print("NO")
else:
    if year % 100 != 0: print("YES")
    else:
        if year % 400 == 0: print("YES")
        else: print("NO")