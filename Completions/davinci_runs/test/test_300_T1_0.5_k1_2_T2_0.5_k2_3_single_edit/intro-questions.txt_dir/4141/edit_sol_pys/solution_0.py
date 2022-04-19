
n = int(input())
print("ACL" + ("" if n % 2 == 0 else "AB") + ("" if n % 3 == 0 else "AC") + ("" if n % 5 == 0 else "AB"))
