
n, k = map(int, input().split())
throws = input().split()

current_student = 1
current_throw = 0


while current_throw < k:
    if throws[current_throw].isdigit():
        current_student = (current_student + int(throws[current_throw])) % n
        current_throw += 1
    else:
        m = int(throws[current_throw][5:])
        for _ in range(m):
            current_throw -= 1
            if throws[current_throw].isdigit():
                current_student = (current_student - int(throws[current_throw])) % n
            else:
                m = int(throws[current_throw][5:])
                for _ in range(m):
                    current_throw -= 1
                    current_student = (current_student + int(throws[current_throw])) % n

print(current_student)
