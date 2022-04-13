

def main():
    """
    This is the main function
    """
    num_inputs = int(input())
    costum_dict = {}
    for i in range(num_inputs):
        costume = input()
        if costume in costumes_dict:
            costumes_dict[costume] += 1
        else:
            costumes_dict[costume] = 1
    max_costumes = max(costumes_dict.values())
    for costume in costumes_dict:
        if costumes_dict[costume] == max_costumes:
            print(costume)

if __name__ == "__main__":
    main()
