import os

path = 'C:\\Users\\77056\\Desktop\\check.txt'

print(f'Check existence: {os.path.exists(path)}')
print('Check existence:', os.access(path, os.F_OK))
print('Check readability:', os.access(path, os.R_OK))
print('Check writability:', os.access(path, os.W_OK))
print('Check executability:', os.access(path, os.X_OK))
os.remove(path)
print(f'Check existence again: {os.path.exists(path)}')