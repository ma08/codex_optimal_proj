def get_data(file_name):
    with open(file_name, 'r') as file:
        data = file.read()
    return data


def write_data(file_name, data):
    with open(file_name, 'w') as file:
        file.write(data)

def append_data(file_name, data):
    with open(file_name, 'a') as file:
        file.write(data)

def get_data_list(file_name):
    with open(file_name, 'r') as file:
        data = file.readlines()
    return data

if __name__ == '__main__':
    file_name = 'data.txt'
    data = get_data(file_name)
    print(data)
    write_data(file_name, 'Hello\n')
    append_data(file_name, 'Hello\n')
    data = get_data_list(file_name)
    print(data)
