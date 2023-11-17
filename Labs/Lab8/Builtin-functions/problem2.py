def calculate_letters(word):
    upper, lower = 0, 0
    for e in word:
        if 'a' <= e and e <= 'z': lower += 1
        if 'A' <= e and e <= 'Z': upper += 1
    print(f'Number of upper letters: {upper}, number of lower letters: {lower}.')
    
#phrase = 'Hello world!'
#calculate_letters(phrase) 