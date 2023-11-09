import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

patterns = 'a.*?b$'

for line in lines:
    re.sub("[ ,.]", ":", line)
    
with open('text.txt', 'w') as fp:
    for line in lines:
        fp.write(line + '\n')
    
file.close()