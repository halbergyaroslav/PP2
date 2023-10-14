import itertools

def permutations(s):
    s = list(s)
    return ' '.join(str(''.join(e)) for e in list(itertools.permutations(s)))

#print(permutations('abcd'))