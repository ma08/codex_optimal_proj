

regex_pattern = r"\d{2}[-]\d{2}[-]\d{4}"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
