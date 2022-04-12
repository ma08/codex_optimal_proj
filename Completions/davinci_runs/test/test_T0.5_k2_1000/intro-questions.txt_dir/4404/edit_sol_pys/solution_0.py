
from datetime import datetime

def main():
    # Input
    s = input()

    # Convert
    date = datetime.strptime(s, '%Y/%m/%d')

    # Process
    if date <= datetime(2019, 4, 30):
        print('Heisei')
    else:
        print('TBD')

if __name__ == "__main__":
    main()
