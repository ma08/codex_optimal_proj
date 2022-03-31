

def check_num(num: str) -> bool:
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            for k in range(j + 1, len(num)):
                if num[i] != num[j] and num[j] != num[k] and num[k] != num[i]:
                    return True
    return False

print("Yes" if check_num(input()) else "No")