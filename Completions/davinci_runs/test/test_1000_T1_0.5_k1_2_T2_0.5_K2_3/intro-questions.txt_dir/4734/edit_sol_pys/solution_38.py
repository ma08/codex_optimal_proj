

import re

while True:
    input_str = input()
    if input_str == '.':
        break
    print(re.match(r'^[a-zA-Z][a-zA-Z0-9]*$', input_str))
