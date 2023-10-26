def generator(n):
    value = 2
    while value < n:
        yield str(value)
        value += 2
        if value < n: yield ', '

#n = int(input())    
#for value in generator(n):
#    print(value, end = '')