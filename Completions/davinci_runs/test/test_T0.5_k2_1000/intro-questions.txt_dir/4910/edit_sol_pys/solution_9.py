

def main():
    """
    This is the main function
    """
    num_inputs = int(input())
    costume_dict = {}
    for i in range(num_inputs):
        costume = input()
        if costume in costume_dict:
            costume_dict[costume] += 1
        else:
            costume_dict[costume] = 1
    max_costumes = max(costume_dict.values())
    for costume in costume_dict:
        if costume_dict[costume] == max_costumes:
            print(costume)

if __name__ == "__main__":
    main()
