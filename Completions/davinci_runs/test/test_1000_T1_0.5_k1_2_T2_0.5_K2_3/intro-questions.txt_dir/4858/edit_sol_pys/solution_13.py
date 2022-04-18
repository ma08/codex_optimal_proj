

import sys

def read_input(path):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def write_output(path, output):
    with open(path, 'w') as f:
        f.write(output)

def solve(lines):
    m, n, c = lines[0].split()
    m, n = int(m), int(n)
    first_frame = lines[1:m+1]
    second_frame = lines[m+1:3*m+1]
    result = []
    for i in range(m):
        result.append('')
        for j in range(N):
            if first_frame[i][j] == C:
                if second_frame[i][j] == C:
                    result[i] += C
                else:
                    result[i] += second_frame[i][j]
            else:
                result[i] += first_frame[i][j]
    return '\n'.join(result)

def main():
    lines = read_input(sys.argv[1])
    output = solve(lines)
    write_output(sys.argv[2], output)

if __name__ == '__main__':
    main()
