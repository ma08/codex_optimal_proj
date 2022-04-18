

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

print(lines)
