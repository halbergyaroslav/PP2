import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

pattern = '[A-Z]+[a-z]+$'

for line in lines:
    findings = re.search(pattern, line)
    if findings: print(findings.string)

file.close()