import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()
    
for line in lines:
    print(re.findall('[A-Z][^A-Z]*', line))

file.close()