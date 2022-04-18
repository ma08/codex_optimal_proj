

def check_proof(proof_lines):
    assumptions = []
    for line in proof_lines:
        line = line.split('->')
        if line[0].strip() == '':
            assumptions.append(line[1].strip())
        else:
            for assumption in line[0].split():
                if assumption not in assumptions:
                    return proof_lines.index(line) + 1
            if line[1].strip() not in assumptions:
                assumptions.append(line[1].strip())
    return 'correct'

if __name__ == '__main__':
    n = int(input())
    proof_lines = []
    for _ in range(n):
        proof_lines.append(input())
    print(check_proof(proof_lines))
