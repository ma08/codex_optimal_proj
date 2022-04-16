

def main():
    """
    This is the main function
    """
    num_inputs = int(input())
    costumes = {}
    for i in range(num_inputs):
        costume = input()
        if costume in costumes:
            costumes[costume] += 1
        else:
            costumes[costume] = 1
    max_costumes = max(costumes.values())
    for costume in costumes:
        if costumes[costume] == max_costumes:
            print(costume)

if __name__ == "__main__":
    main()
