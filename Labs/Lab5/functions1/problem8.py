def spy_game(nums):
    print('007' in ''.join(str(e) for e in nums if e == 7 or e == 0))
    
#spy_game([1,2,4,0,0,7,5])
#spy_game([1,0,2,4,0,5,7])
#spy_game([1,7,2,0,4,5,0])