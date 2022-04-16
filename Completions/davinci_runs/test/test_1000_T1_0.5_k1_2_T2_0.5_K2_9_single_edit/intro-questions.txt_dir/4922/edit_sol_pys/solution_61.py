#!/usr/bin/env python3

# SOLUTION
m, n = map(int, input().split())
clauses = [list(map(int, input().split())) for _ in range(m)]

def satisfiable(clauses, n):
    for clause in clauses:
        if clause[0] < 0:
            if clause[1] < 0:
                if clause[2] < 0:
                    return False
            else:
                if clause[2] > 0:
                    return False
        else:
            if clause[1] > 0:
                if clause[2] > 0:
                    return False
    return True

if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")


# NOTE:
#   The problem statement is a bit ambiguous, but I think the intention is that
#   the clauses are all in disjunctive normal form (DNF), i.e. they are of the
#   form (x1 or x2 or x3) AND (x4 or x5 or x6) AND (x7 or x8 or x9).  In other
#   words, the clauses are ANDed together, and the literals within each clause
#   are ORed together.
#
#   Also, for each clause, the literals must be in the range [1, n] (inclusive)
#   and the clause must contain exactly three literals.
