

regex_pattern = r"^[a-z]{0,3}\d{2,8}[A-Z]{3,}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
