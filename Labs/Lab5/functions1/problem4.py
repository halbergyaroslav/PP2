import math

def check_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n) + 1), 1):
        if n % i == 0: return False
    return True

def filter(list):
    return ' '.join(str(e) for e in list if check_prime(e))

#print(filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))