import os

path = 'C:\\Users\\77056\\Desktop\\'

print(f"Only directories: {[x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x)) ]}")
print(f"Only files: {[x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x)) ]}")
print(f"All directories and files: {[x for x in os.listdir(path)]}")