import sys

month_map = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

def is_halloween(month, day):
    return (month == 10 and day == 31) or (month == 11 and day == 25)

line = sys.stdin.readline()
month, day = line.split()
if is_halloween(month_map[month], int(day)):
    print('yup')
else:
    print('nope')
