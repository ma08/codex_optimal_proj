

def main():
    mod = {}
    for i in range(10):
        mod[i] = int(input()) % 42
    print(len(set(mod.values())))

main()
