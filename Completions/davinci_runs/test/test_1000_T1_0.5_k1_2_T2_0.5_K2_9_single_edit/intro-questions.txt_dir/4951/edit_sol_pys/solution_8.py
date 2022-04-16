

def check_proof(proof):
    assumptions = []
    for line in proof:
        line = line.split('|-')
        if line[0].strip() == ' ':
            assumptions.append(line[1].strip().replace(' ', ''))
        else:
            for assumption in line[0].split(' '):
                if assumption not in assumptions:
                    return proof.index(line) + 1, assumption
            assumptions.append(line[1].strip().replace(' ', ''))
    return 'correct'

if __name__ == '__main__':
    n = int(input().replace(' ', ''))
    proof = []
    for _ in range(n):
        proof.append(input().replace(' ', ''))
    print(check_proof(proof))
