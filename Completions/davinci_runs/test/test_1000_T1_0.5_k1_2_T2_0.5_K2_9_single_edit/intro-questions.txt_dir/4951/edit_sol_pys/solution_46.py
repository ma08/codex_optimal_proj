
def check_proof(lines):
    assumptions = []
    for line in lines:
        line = line.split('->')
        if line[0].strip() == '':
            assumptions.append(line[1].strip())
        else:
            for assumption in line[0].split():
                if assumption not in assumptions:
                    return lines.index(line) + 1
            assumptions.append(line[1].strip())
    return 'correct'

if __name__ == '__main__':
    n = int(input())
    lines = []
    for _ in range(n):
        lines.append(input())
    print(check_proof(lines))
