import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

for i in range(len(lines)):
    lines[i] = re.sub("[ ,.]", ":", lines[i])

with open('text.txt', 'w', encoding="utf8") as fp:
    for line in lines:
        fp.write(line + '\n')
    
file.close()