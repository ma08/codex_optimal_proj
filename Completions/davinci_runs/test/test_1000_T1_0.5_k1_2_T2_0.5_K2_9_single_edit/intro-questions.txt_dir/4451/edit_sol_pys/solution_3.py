import csv
from datetime import datetime


def read_csv(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


def write_csv(file, data):
    with open(file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def read_file(file):
    with open(file, 'r') as f:
        reader = f.readlines()
        print(reader)


def write_file(file, data):
    with open(file, 'w') as f:
        f.write(data)


def main():
    read_csv('example.csv')
    write_csv('example.csv', ['hello', 'world', '!'])
    read_file('example.txt')
    write_file('example.txt', 'hello world!')


if __name__ == '__main__':
    main()
