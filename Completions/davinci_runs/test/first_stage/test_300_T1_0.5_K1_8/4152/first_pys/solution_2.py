

def main():
    """
    Для каждого элемента последовательности необходимо найти другой элемент, являющийся суммой степени двойки.
    При этом необходимо учитывать то, что некоторые элементы могут повторяться.
    Поэтому надо представить последовательность в виде множества, где каждый элемент представлен в виде кортежа
    (элемент, количество повторений).
    После этого надо найти для каждого элемента последовательности другой элемент, являющийся суммой степени двойки.
    Для этого нужно проверить, есть ли в множестве элемент, являющийся разностью степени двойки и текущего элемента.
    Если такой элемент есть, то он и будет нужным.
    Если такого элемента нет, то нужно проверить, есть ли в множестве элемент, являющийся суммой степени двойки и текущего элемента.
    Если такой элемент есть, то он и будет нужным.
    Если ни одного такого элемента нет, то нужно удалить данный элемент.
    После этого нужно проверить, что данный элемент и найденный элемент не являются одним и тем же.
    Если это так, то нужно удалить копию данного элемента.
    Если это не так, то нужно удалить одну копию данного элемента и одну копию найденного элемента.
    После этого надо проверить, что количество копий данного элемента и найденного элемента не превышает 1.
    Если это так, то нужно удалить оставшиеся копии.
    После этого нужно проверить, что в множестве не осталось ни одного элемента.
    Если это так, то нужно прибавить 1 к количеству удаленных элементов.
    После этого надо проверить, что в множестве остался только один элемент.
    Если это так, то нужно проверить, что этот элемент является степенью двойки.
    Если это так, то нужно прибавить 1 к количеству удаленных элементов.
    После этого надо вывести количество удаленных элементов.
    """
    n = int(input())
    sequence = list(map(int, input().split()))
    elements = set()
    for element in sequence:
        elements.add((element, sequence.count(element)))
    removed_elements = 0
    for element, element_count in elements:
        if element in elements:
            for i in range(30):
                power_of_two = 2 ** i
                if power_of_two - element in elements:
                    if element == power_of_two - element:
                        if element_count > 1:
                            elements.remove((element, element_count))
                            removed_elements += 1
                        break
                    else:
                        if element_count > 1:
                            elements.remove((element, element_count))
                            element_count -= 1
                        if elements.count((power_of_two - element, elements.count((power_of_two - element, 0)))) > 1:
                            elements.remove((power_of_two - element, elements.count((power_of_two - element, 0))))
                            elements.add((power_of_two - element, elements.count((power_of_two - element, 0)) - 1))
                        break
                elif power_of_two + element in elements:
                    if element == power_of_two + element:
                        if element_count > 1:
                            elements.remove((element, element_count))
                            removed_elements += 1
                        break
                    else:
                        if element_count > 1:
                            elements.remove((element, element_count))
                            element_count -= 1
                        if elements.count((power_of_two + element, elements.count((power_of_two + element, 0)))) > 1:
                            elements.remove((power_of_two + element, elements.count((power_of_two + element, 0))))
                            elements.add((power_of_two + element, elements.count((power_of_two + element, 0)) - 1))
                        break
            else:
                removed_elements += 1
                elements.remove((element, element_count))
    if len(elements) == 0:
        removed_elements += 1
    elif len(elements) == 1:
        element, element_count = elements.pop()
        if element_count == 1:
            for i in range(30):
                if element == 2 ** i:
                    removed_elements += 1
    print(removed_elements)

if __name__ == "__main__":
    main()