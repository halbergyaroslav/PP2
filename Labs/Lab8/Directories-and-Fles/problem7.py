import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

with open('text.txt', 'w', encoding="utf8") as fp:
    for line in lines:
        fp.write(line)
    
file.close()