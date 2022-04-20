import sys
from collections import deque
from itertools import combinations
from math import sqrt
from heapq import heapify, heappop, heappush
from bisect import bisect_left
from copy import deepcopy
from fractions import gcd
from random import randint
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from functools import reduce
from bisect import bisect_left
from math import sqrt
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase
from datetime import datetime
from operator import itemgetter
from fractions import gcd
from random import randint
from bisect import bisect_left
from heapq import heappop, heappush
from collections import Counter
from collections import deque
from itertools import combinations
from functools import reduce
from math import gcd
from decimal import Decimal
from copy import deepcopy
from string import ascii_lowercase, asci

import sys

def main():
    n, a, b, c = map(int, sys.stdin.readline().split())
    l = [int(sys.stdin.readline()) for _ in range(n)]
    l.sort()
    ans = float("inf")
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] < a and l[j] < b and l[k] < c:
                    ans = min(ans, (a - l[i]) + (b - l[j]) + (c - l[k]))
    print(ans)

if __name__ == '__main__':
    main()
