

def main():
    """This is the main function"""
    num_inputs = int(input())
    costum_dict = {}
    for i in range(num_inputs):
        costume = input()
        if costume in costum_dict:
            costum_dict[costume] += 1
        else:
            costum_dict[costume] = 1
    max_costumes = max(costum_dict.values())
    for costume in costum_dict:
        if costum_dict[costume] == max_costumes:
            print(costume)

if __name__ == "__main__":
    main()
