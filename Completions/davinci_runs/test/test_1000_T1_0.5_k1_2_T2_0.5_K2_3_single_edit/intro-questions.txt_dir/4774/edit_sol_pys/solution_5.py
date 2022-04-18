

# The solution is pretty straightforward.
# We use a list of operators, and then use a list comprehension to generate all possible expressions.
# Then, we filter out the ones that are not valid.
# Finally, we sort them alphabetically, and print them.

a, b, c, d = [int(x) for x in input().split()]

operators = ["+","-","*","/"]

expressions = [f"{a} {i} {b} = {c} {j} {d}" for i in operators for j in operators]

expressions = [x for x in expressions if eval(x.replace("=","=="))]

if len(expressions) == 0:
    print("problems ahead")
else:
    print("\n".join(sorted(expressions)))
