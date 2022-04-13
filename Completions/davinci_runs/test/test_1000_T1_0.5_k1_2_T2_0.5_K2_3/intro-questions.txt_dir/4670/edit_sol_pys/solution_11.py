

regex_pattern = r"^[a-zA-Z02468]{40}[13579\s]{5}$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
