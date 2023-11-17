def check_tuple(array):
    ans = 1
    for e in array:
        if not e: ans = 0
    return bool(ans)
    
#tuple = ('Malika', 'Yaroslav', 'Eva', 'Kamal', 'Gania', 'Amira')
#print(check_tuple(tuple))
#tuple = ('Malika', 'Yaroslav', 'Eva', 'Kamal', 'Gania', 'Amira', 0)
#print(check_tuple(tuple))