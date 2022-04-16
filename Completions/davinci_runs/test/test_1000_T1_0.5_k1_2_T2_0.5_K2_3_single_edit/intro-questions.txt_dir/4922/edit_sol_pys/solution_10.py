

"""
The problem is to determine if a 3-SAT instance with m clauses and n variables is satisfiable.

The input is the number of clauses m, the number of variables n, and the m clauses. Each clause consists of 3 distinct space-separated integers in the range [−n, n] \ {0}. For each clause, the three values correspond to the three literals in the clause. If the literal is negative, that means that the clause is satisfied if the corresponding variable is set to False, and if it is positive the clause is satisfied if the variable is set to True.

A 3-SAT instance with m clauses and n variables is satisfiable if there is a way to assign values to the n variables such that all m clauses are satisfied.

An example of a 3-SAT instance is shown below (from sample input 1):

# (¬x
# 1
# ∨x
# 2
# ∨x
# 3
# )∧(¬x
# 1
# ∨¬x
# 2
# ∨x
# 3
# )∧(x
# 1
# ∨¬x
# 2
# ∨x
# 3
# )∧(x
# 1
# ∨¬x
# 2
# ∨¬x
# 3
# )∧(x
# 1
# ∨x
# 2
# ∨¬x
# 3
# )

The output is “satisfactory” if the 3-SAT instance is satisfiable, and “unsatisfactory” otherwise.

The judge Øyvind hates 3-SAT instances with less than eight clauses – as these are always satisfiable they provide no real challenge for the contestants. Therefore, he will deem such problem instances to be unsatisfactory. Whenever Øyvind encounters an instance with eight or more clauses he knows that it is a real challenge to figure out whether this instance is satisfiable or not – and therefore he will judge these problem instances to be satisfactory.

Given an instance of 3-SAT, can you help find Øyvind’s judgement?
"""

#n = number of variables
#m = number of clauses

#get input
m, n = map(int, input().split())
clauses = []
for i in range(m):
    clauses.append(list(map(int, input().split())))

#check if it is unsatisfactory
if m < 8:
    print("unsatisfactory")
else:
    print("satisfactory")
