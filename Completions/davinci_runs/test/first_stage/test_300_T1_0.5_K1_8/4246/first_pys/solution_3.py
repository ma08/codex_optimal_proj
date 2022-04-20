

def main():
    forecast = list(input())
    actual = list(input())
    days = 0
    for i in range(len(forecast)):
        if forecast[i] == actual[i]:
            days += 1
    print(days)

if __name__ == '__main__':
    main()