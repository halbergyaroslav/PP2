import re

with open('row.txt', 'r', encoding="utf8") as file:
    lines = file.readlines()

patterns = '^a(b*)$'

for line in lines:
    findings = re.search(patterns, line)
    if findings: print(findings.string)

file.close()