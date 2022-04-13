
def check_proof(proof_lines):
    assumptions = []
    for line in proof_lines:
        if '|-' in line:
            assumptions.append(line.split('|-')[0].strip())
        else:
            line = line.split('->')
            if line[0].strip() == '':
                assumptions.append(line[1].strip())
            else:
                for assumption in line[0].split():
                    if assumption not in assumptions:
                        return proof_lines.index(line) + 1
                assumptions.append(line[1].strip())
    return 'correct'

if __name__ == '__main__':
    n = int(input())
    proof_lines = []
    for _ in range(n):
        proof_lines.append(input())
    print(check_proof(proof_lines))
