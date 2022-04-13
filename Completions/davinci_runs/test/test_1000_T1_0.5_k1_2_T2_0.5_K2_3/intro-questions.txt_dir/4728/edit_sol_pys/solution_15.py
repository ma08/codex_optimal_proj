
# print('Enter Input')
from collections import Counter

# inp = input().split()
# inp_molecule = Counter(inp[0])
# inp_molecule['C'] = inp_molecule.get('C', 0) * int(inp[1])
# print('Enter Output')
# out_molecule = Counter(input())

# print(inp_molecule)
# print(out_molecule)

# print(inp_molecule.get('C', 0))
# print(out_molecule.get('C', 0))

# if inp_molecule.get('C', 0) >= out_molecule.get('C', 0):
#     if inp_molecule.get('H', 0) >= out_molecule.get('H', 0):
#         print(int(inp_molecule.get('C', 0) / out_molecule.get('C', 0)))
#     else:
#         print(0)
# else:
#     print(0)

import re


def count_substring(string, sub_string):
    count = 0
    while True:
        match = re.search(sub_string, string)
        if match:
            count += 1
            string = string[match.start() + len(sub_string):]
        else:
            return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# from collections import Counter

# inp = input().split()
# inp_molecule = Counter(inp[0])
# inp_molecule['C'] = inp_molecule.get('C', 0) * int(inp[1])
# print('Enter Output')
# out_molecule = Counter(input())

# print(inp_molecule)
# print(out_molecule)

# print(inp_molecule.get('C', 0))
# print(out_molecule.get('C', 0))

# if inp_molecule.get('C', 0) >= out_molecule.get('C', 0):
#     if inp_molecule.get('H', 0) >= out_molecule.get('H', 0):
#         print(int(inp_molecule.get('C', 0) / out_molecule.get('C', 0)))
#     else:
#         print(0)
# else:
#     print(0)
