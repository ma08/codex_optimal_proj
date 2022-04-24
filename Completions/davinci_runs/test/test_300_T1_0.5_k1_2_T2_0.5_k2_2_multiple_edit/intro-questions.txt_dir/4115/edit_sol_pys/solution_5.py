s = input()
if s == s[::-1]:  # 회문이면 0 출력
    print(0)
    exit()  # 종료
for i in range(len(s) // 2):
    if s[i] == s[-1 - i]:
        continue
    else:  # 한 글자만 다르면 1 출력
        print(1)
        break
else:
    print(1)  # 모두 같으면 1 출력
