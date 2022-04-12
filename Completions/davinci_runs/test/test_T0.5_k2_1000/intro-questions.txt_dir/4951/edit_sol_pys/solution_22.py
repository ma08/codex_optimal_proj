

def check_proof(proof_list):
    assumptions = []
    for line in proof_list:
        line = line.split('->')
        if line[0].strip() == '':
            assumptions.append(line[1].strip())
        else:
            for assumption in line[0].split():
                if assumption not in assumptions:
                    return proof_list.index(line) + 1
            assumptions.append(line[1].strip())
    return 'correct'

if __name__ == '__main__':
    n = int(raw_input())
    proof_list = []
    for _ in range(n):
        proof_list.append(raw_input())
    print(check_proof(proof_list))
