import math

def read_file(filename):
    with open(filename) as input_file:
        data = input_file.readlines()
    return data


def write_file(filename, data):
    with open(filename, 'w') as output_file:
        output_file.write(data)


def process_data(data):
    return data


def main():
    data = read_file('file.in')
    processed_data = process_data(data)
    write_file('file.out', processed_data)


if __name__ == '__main__':
    main()


n = int(input())

vaccinated = []
control = []

for i in range(n):
    line = input()
    if line[0] == 'Y':
        vaccinated.append(line)
    else:
        control.append(line)

strains = ['A', 'B', 'C']

for strain in strains:
    count = 0
    for person in vaccinated:
        if person[strains.index(strain) + 1] == 'Y':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate = count / len(vaccinated)
    count = 0
    for person in control:
        if person[strains.index(strain) + 1] == 'Y':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate2 = count / len(control)
    print(100 - (rate / rate2 * 100))
