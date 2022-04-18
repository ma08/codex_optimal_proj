

def check_proofs(proof):
    assumptions = []
    try:
        for line in proof:
            line = line.split('->')
            if line[0].strip() == '':
                assumptions.append(line[1].strip())
            else:
                for assumption in line[0].split():
                    if assumption not in assumptions:
                        return proof.index(line) + 1
                assumptions.append(line[1].strip())
        return 'correct'
    except IndexError:
        return proof.index(line) + 1


if __name__ == '__main__':
    n = int(input())
    proof = []
    for _ in range(n):
        proof.append(input())
    print(check_proofs(proof))
