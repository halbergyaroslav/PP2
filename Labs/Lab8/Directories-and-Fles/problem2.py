import os

print('Check existence:', os.access('C:\\Users\\77056\\Desktop\\', os.F_OK))
print('Check readability:', os.access('C:\\Users\\77056\\Desktop\\', os.R_OK))
print('Check writability:', os.access('C:\\Users\\77056\\Desktop\\', os.W_OK))
print('Check executability:', os.access('C:\\Users\\77056\\Desktop\\', os.X_OK))