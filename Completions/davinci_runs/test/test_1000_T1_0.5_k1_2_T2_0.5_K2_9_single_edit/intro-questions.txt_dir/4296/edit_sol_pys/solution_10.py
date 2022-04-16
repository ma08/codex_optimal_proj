

a1,a2,a3 = map(int, input().split())

if a1+a2+a3 >= 22: # もし、a1とa2とa3の和が22以上ならば
    print('bust')
else: # そうでなければ
    print('win')
