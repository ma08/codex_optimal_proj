

def main():
    """
    This is the main function
    """
    num_inputs = int(input())
    customer_dict = {}
    for i in range(num_inputs):
        customer = input()
        if customer in customer_dict:
            customer_dict[customer] += 1
        else:
            customer_dict[customer] = 1
    max_customers = max(customer_dict.values())
    for customer in customer_dict:
        if customer_dict[customer] == max_customers:
            print(customer)

if __name__ == "__main__":
    main()
