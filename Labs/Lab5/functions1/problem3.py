def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens = numheads - rabbits
    
    return f"chickens: {chickens}, rabbits: {rabbits}"

#sprint(solve(35, 94))