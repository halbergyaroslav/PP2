import math

def check_prime(n):
    if n == 1: return False
    else:
        for i in range(2, math.floor(math.sqrt(n) + 1), 1):
            if n % i == 0: return False
    return True

class Filter_Prime:
    def __init__(self, list_primes):
        self.list_primes = list_primes
    
    def return_prime(self):
        self.list_primes = filter(lambda x: check_prime(x), self.list_primes)
        return list(self.list_primes)



#list_primes = Filter_Prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#print(list_primes.return_prime())