

S = input()
S_list = list(S)
S_list.sort()

if S_list == ['a', 'b', 'c'] or S_list == ['a', 'c', 'b'] or S_list == ['b', 'a', 'c'] or S_list == ['b', 'c', 'a'] or S_list == ['c', 'a', 'b'] or S_list == ['c', 'b', 'a']:
    print("Yes")
else:
    print("No")
