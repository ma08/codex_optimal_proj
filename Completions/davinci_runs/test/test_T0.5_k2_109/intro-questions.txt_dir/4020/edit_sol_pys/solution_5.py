
h1, m1 = map(int, input().split(':'))  # вводим время начала
h2, m2 = map(int, input().split(':'))  # вводим время конца

if m1 % 2 == 0:  # если минуты начала четные
    m_mid = m1 + ((m2 - m1) // 2)
else:  # если минуты начала нечетные
    m_mid = m1 + ((m2 - m1) // 2) + 1

h_mid = h1 + ((m_mid - m1) // 60)  # получаем часы

print(f'{h_mid:02d}:{m_mid:02d}')
