

s = input()

if s[0] == "A" and s[2:-1].count("C") == 1 and s[1].islower():
    for i in range(1, len(s)):
        if s[i] == "C":
            continue
        elif s[i].islower():
            print("AC")  # Accepted
            break
        else:
            print("WA")  # Wrong Answer
            break
else:
    print("WA")  # Wrong Answer
