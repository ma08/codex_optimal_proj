

regex_pattern = r"^[123][120][xs0][30Aa][xsu][\.,]$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))
