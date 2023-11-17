import os

path = 'C:\\Users\\77056\\Desktop\\check.txt'

print(f'Check existence: {os.path.exists(path)}')
print(f'Filename of the given path: {os.path.basename(path)}')
print(f'Directory partion of the given path: {os.path.dirname(path)}')