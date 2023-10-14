def unique(array):
    ans = list()
    for e in array:
        if e not in ans: ans.append(e)
    return ans
        
#print(unique([1, 2, 3, 4, 1, 6, 7, 4, 6]))