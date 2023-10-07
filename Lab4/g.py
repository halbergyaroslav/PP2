n = int(input())
nums = set(range(1, n + 1))
ans = nums
while True:
    s = input()
    if s == 'HELP': break
    s = {int(x) for x in s.split()}
    answer = input()
    if answer == 'YES': ans &= s
    else: ans &= nums - s

print(' '.join([str(x) for x in sorted(ans)]))