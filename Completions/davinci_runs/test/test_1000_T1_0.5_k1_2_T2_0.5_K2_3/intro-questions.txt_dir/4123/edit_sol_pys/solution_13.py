


def solve(s):
    """
    >>> solve('AC')
    'AC'
    >>> solve('Z')
    'Z'
    >>> solve('A')
    'A'
    >>> solve('AZ')
    'A'
    >>> solve('ZA')
    'Z'
    >>> solve('ZAZ')
    'ZA'
    >>> solve('AAZZ')
    'AZ'
    >>> solve('AZA')
    'AA'
    >>> solve('ZAZA')
    'ZA'
    >>> solve('ZZZA')
    'ZZ'
    >>> solve('ZZAZ')
    'ZZ'
    >>> solve('AZZZ')
    'AZ'
    >>> solve('AAZZZ')
    'AZ'
    >>> solve('AZZZA')
    'AZ'
    >>> solve('ZZAZA')
    'ZZ'
    >>> solve('ZZAZZ')
    'ZZ'
    >>> solve('AZZZZ')
    'AZ'
    >>> solve('AAZZZZ')
    'AZ'
    >>> solve('AZZZZZ')
    'AZ'
    >>> solve('ZZAZZZ')
    'ZZ'
    >>> solve('ZZAZZA')
    'ZZ'
    >>> solve('ZZAZAZ')
    'ZZ'
    >>> solve('AZZZZZ')
    'AZ'
    >>> solve('AAZZZZZ')
    'AZ'
    >>> solve('AZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZ')
    'ZZ'
    >>> solve('ZZAZZZA')
    'ZZ'
    >>> solve('ZZAZAZZ')
    'ZZ'
    >>> solve('ZZAZAZA')
    'ZZ'
    >>> solve('AZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZ')
    'ZZ'
    >>> solve('ZZAZAZZA')
    'ZZ'
    >>> solve('ZZAZAZAZ')
    'ZZ'
    >>> solve('AZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZZ')
    'ZZ'
    >>> solve('ZZAZAZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZZ')
    'ZZ'
    >>> solve('ZZAZAZAZA')
    'ZZ'
    >>> solve('AZZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZ')
    'ZZ'
    >>> solve('AZZZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZZ')
    'ZZ'
    >>> solve('ZZAZAZAZAZA')
    'ZZ'
    >>> solve('AZZZZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZAZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZAZ')
    'ZZ'
    >>> solve('AZZZZZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZAZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZAZZ')
    'ZZ'
    >>> solve('ZZAZAZAZAZAZA')
    'ZZ'
    >>> solve('AZZZZZZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZZZZZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZZZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZZZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZZZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZZZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZZZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZAZZZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZAZZZ')
    'ZZ'
    >>> solve('ZZAZAZAZAZAZZA')
    'ZZ'
    >>> solve('ZZAZAZAZAZAZAZ')
    'ZZ'
    >>> solve('AZZZZZZZZZZZZZ')
    'AZ'
    >>> solve('AAZZZZZZZZZZZZZ')
    'AZ'
    >>> solve('AZZZZZZZZZZZZZZ')
    'AZ'
    >>> solve('ZZAZZZZZZZZZZZZ')
    'ZZ'
   
    """
    counter = dict()
    for i in range(len(s) - 1):
        two_gram = s[i:i+2]
        counter[two_gram] = counter.get(two_gram, 0) + 1
    max_value = max(counter.values())
    for k, v in counter.items():
        if v == max_value:
            return k


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = solve(s)
    print(result)
