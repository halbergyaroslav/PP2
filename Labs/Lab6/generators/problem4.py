def generator(a, b):
    value = a
    while (value < b):
        yield value * value
        value += 1

a, b = input().split(' ')
a, b = int(a), int(b)

for value in generator(a, b):
    print(value, end = ' ')
