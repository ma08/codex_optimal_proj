

def main():
    num_inputs = int(input())
    costumer_dict = {}
    for i in range(num_inputs):
        costumer = input()
        if costumer in costumer_dict:
            costumer_dict[costumer] += 1
        else:
            costumer_dict[costumer] = 1
    max_costumers = max(costumer_dict.values())
    for costumer in costumer_dict:
        if costumer_dict[costumer] == max_costumers:
            print(costumer)

if __name__ == "__main__":
    main()
