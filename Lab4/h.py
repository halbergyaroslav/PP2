n = int(input())
nums = set(range(1, n + 1))
ans = nums
while True:
    s = input()
    if s == 'HELP': break
    s = {int(x) for x in s.split()}
    
    if len(ans & s) > len(ans) / 2:
        print("YES")
        ans &= s
    else:
        print("NO")
        ans &= nums - s

print(' '.join([str(x) for x in sorted(ans)]))