def camel_to_snake(line):
        import re
        str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', line)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str).lower()

print(camel_to_snake(input()))