from time import sleep
from math import sqrt

def calculate_sqrt(number, delay):
    sleep(delay / 1000)
    print(f'Square root of {number} after {delay} miliseconds is {sqrt(number)}')
    
#calculate_sqrt(int(input()), int(input()))