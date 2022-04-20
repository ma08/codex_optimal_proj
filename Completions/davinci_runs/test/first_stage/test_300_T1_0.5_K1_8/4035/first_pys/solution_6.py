

#-----main()-----
def main():
    #get input
    a, b = map(int, input().split())

    #to find the price, divide A and B by 0.08 and 0.1, respectively.
    #to find the minimum price, divide A and B by 0.08 and 0.1, respectively, and find the maximum of these values.
    #if the maximum is less than or equal to 0, there is no answer.
    #if the maximum is greater than 0, the minimum price is the maximum value.
    max_price = max(a / 0.08, b / 0.1)
    if max_price <= 0:
        print(-1)
    else:
        print(int(max_price))

if __name__ == '__main__':
    main()