import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

print(len(lines))

file.close()