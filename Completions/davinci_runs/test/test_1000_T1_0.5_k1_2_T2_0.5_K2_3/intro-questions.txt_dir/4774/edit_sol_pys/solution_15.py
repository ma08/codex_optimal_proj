



a,b,c,d = [int(x) for x in input().split()]

operators = ["+","-","*","/"]

expressions = [f"{a} {i} {b} = {c} {j} {d}" for i in operators for j in operators]

expressions = [x for x in expressions if eval(x.replace("=","==")) != False]

if len(expressions) == 0:
    print("problems ahead")
else:
    print("\n".join(sorted(expressions)))
