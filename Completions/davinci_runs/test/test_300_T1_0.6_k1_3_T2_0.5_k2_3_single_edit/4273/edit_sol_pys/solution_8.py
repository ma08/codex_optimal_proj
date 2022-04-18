
import sys
import itertools

def main():
    N = int(input())
    names = [input() for _ in range(N)]
    names_dict = {}
    for name in names:
        if name[0] in ["M", "A", "R", "C", "H"] and len(name) in [1, 2, 3, 4, 5]:
            if name[0] not in names_dict:
                names_dict[name[0]] = []
            names_dict[name[0]].append(name)
    names_dict["M"].sort()
    names_dict["A"].sort()
    names_dict["R"].sort()
    names_dict["C"].sort()
    names_dict["H"].sort()
    ans = 0
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 2):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 2):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 2):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 2):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 2):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 2):
        for d in itertools.combinations(names_dict["A"], 2):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 2):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 2):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 2):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 2):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 2):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 2):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 2):
            for e in itertools.combinations(names_dict["R"], 2):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 2):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 2):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 2):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 2):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 2):
                for f in itertools.combinations(names_dict["C"], 2):
                    for g in itertools.combinations(names_dict["H"], 1):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 2):
                for f in itertools.combinations(names_dict["C"], 1):
                    for g in itertools.combinations(names_dict["H"], 2):
                        ans += 1
    for c in itertools.combinations(names_dict["M"], 1):
        for d in itertools.combinations(names_dict["A"], 1):
            for e in itertools.combinations(names_dict["R"], 1):
                for f in itertools.combinations(names_dict["C"], 2):
                    for g in itertools.combinations(names_dict["
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
