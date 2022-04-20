

def main():
    """main function"""
    values = [int(x) for x in input().split()]
    n_people = values[0]
    train_cost = values[1]
    taxi_cost = values[2]

    if train_cost * n_people > taxi_cost:
        print(taxi_cost)
    else:
        print(train_cost * n_people)

if __name__ == '__main__':
    main()