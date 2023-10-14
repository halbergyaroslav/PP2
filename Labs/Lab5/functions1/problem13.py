import random

def greeting(name):
    print(f'\nWell, {name}, I am thinking of a number between 1 and 20.\nTake a guess.')

def generate_number():
    global number
    number = random.randint(1, 20)

def guess(n):
    print('\n')
    if n < number:
        print('Your guess is too low.\nTake a guess.')
        return False
    elif n > number:
        print('Your guess is too much.\nTake a guess')
        return False
    return True

def congratulations(name, moves):
    if moves == 1: print(f'Good job, {name}! You guessed my number in {moves} guess!')
    else: print(f'Good job, {name}! You guessed my number in {moves} guesses!')
    
def specially_for_next_task(name):
    print(f'Congratulations, {name}! You successfully imported functions from another file in Python!')
    


def main():
    print('Hello! What is your name?')
    name = input()
    greeting(name)
    generate_number()
    
    n = int(input())
    moves = 1
    while guess(n) != True:
        n = int(input())
        moves += 1
        
    congratulations(name, moves)
        

if __name__ == '__main__':
    main()