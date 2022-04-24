
#!/usr/bin/python3
import re
print(re.sub(r'(?<= )&&(?= )', 'and',
             re.sub(r'(?<= )\|\|(?= )', 'or', input())))
