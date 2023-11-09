import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

patterns = 'ab{2,3}'

for line in lines:
    findings = re.search(patterns, line)
    if findings: print(findings.string)

file.close()