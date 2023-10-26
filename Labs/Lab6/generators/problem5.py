def generator(n):
    value = n
    while (value > -1):
        yield value
        value -= 1

n = int(input())
for value in generator(n):
    print(value, end = ' ')