import math

n = int(input('Input number of sides: '))
a = int(input('Input the length of a side: '))

angle = math.sin(math.radians(180 * (n - 2) / (2 * n)))
central_angle = math.sin(math.radians(360 / n))
b = a * angle / central_angle
print(f'The area of the plygon is: {n * b * b * math.sin(math.radians(360 / n)) / 2}')

#Input number of sides: 4
#Input the length of a side: 25
#The area of the polygon is: 625