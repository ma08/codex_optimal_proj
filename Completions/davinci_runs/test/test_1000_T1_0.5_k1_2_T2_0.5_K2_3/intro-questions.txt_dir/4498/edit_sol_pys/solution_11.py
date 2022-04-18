

a, b, c, d = map(int, input().split())
print('Yes' if d >= abs(a - c) or (d >= abs(a - b) and d >= abs(b - c)) else 'No') 
