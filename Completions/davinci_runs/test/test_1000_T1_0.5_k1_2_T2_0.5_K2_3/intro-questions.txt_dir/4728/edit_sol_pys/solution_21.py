
import sys

if __name__ == '__main__':
    input_molecule = sys.stdin.readline().strip()
    n_input_molecule = int(sys.stdin.readline().strip())
    output_molecule = sys.stdin.readline().strip()

    input_molecule_dict = {}
    for i in range(len(input_molecule)):
        if input_molecule[i].isalpha():
            if i == len(input_molecule) - 1:
                if input_molecule[i] in input_molecule_dict:
                    input_molecule_dict[input_molecule[i]] += 1
                else:
                    input_molecule_dict[input_molecule[i]] = 1
            else:
                if input_molecule[i + 1].isalpha():
                    if input_molecule[i] in input_molecule_dict:
                        input_molecule_dict[input_molecule[i]] += 1
                    else:
                        input_molecule_dict[input_molecule[i]] = 1
                else:
                    if input_molecule[i] in input_molecule_dict:
                        input_molecule_dict[input_molecule[i]] += int(input_molecule[i + 1])
                    else:
                        input_molecule_dict[input_molecule[i]] = int(input_molecule[i + 1])

    output_molecule_dict = {}
    for i in range(len(output_molecule)):
        if output_molecule[i].isalpha():
            if i == len(output_molecule) - 1:
                if output_molecule[i] in output_molecule_dict:
                    output_molecule_dict[output_molecule[i]] += 1
                else:
                    output_molecule_dict[output_molecule[i]] = 1
            else:
                if output_molecule[i + 1].isalpha():
                    if output_molecule[i] in output_molecule_dict:
                        output_molecule_dict[output_molecule[i]] += 1
                    else:
                        output_molecule_dict[output_molecule[i]] = 1
                else:
                    if output_molecule[i] in output_molecule_dict:
                        output_molecule_dict[output_molecule[i]] += int(output_molecule[i + 1])
                    else:
                        output_molecule_dict[output_molecule[i]] = int(output_molecule[i + 1])

    output_molecule_dict_keys = sorted(output_molecule_dict.keys())
    input_molecule_dict_keys = sorted(input_molecule_dict.keys())

    if output_molecule_dict_keys != input_molecule_dict_keys:
        print(0)
        sys.exit()

    output_molecule_list = []
    for i in range(len(output_molecule_dict_keys)):
        output_molecule_list.append(output_molecule_dict[output_molecule_dict_keys[i]])

    input_molecule_list = []
    for i in range(len(input_molecule_dict_keys)):
        input_molecule_list.append(input_molecule_dict[input_molecule_dict_keys[i]])

    if max(output_molecule_list) > max(input_molecule_list):
        print(0)
        sys.exit()

    n_output_molecule = 0
    while n_input_molecule > 0:
        n_input_molecule -= 1
        for i in range(len(output_molecule_list)):
            input_molecule_list[i] -= output_molecule_list[i]

        if min(input_molecule_list) >= 0:
            n_output_molecule += 1
        else:
            break

    print(n_output_molecule)
