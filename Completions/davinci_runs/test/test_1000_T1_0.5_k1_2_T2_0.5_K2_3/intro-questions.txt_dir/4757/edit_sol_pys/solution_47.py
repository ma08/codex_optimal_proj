
def bard(num_villagers, num_evenings):
    """bard"""
    bard_list = []
    bard_list.append(1)
    for _ in range(num_evenings):
        num_villagers_present = int(input())
        villager_list = [int(i) for i in input().split()]
        if 1 in villager_list:
            for i in villager_list:
                if i not in bard_list:
                    bard_list.append(i)
        else:
            for i in villager_list:
                if i not in bard_list:
                    bard_list.append(i)
    bard_list.sort()
    for i in bard_list:
        print(i)

def main():
    """Bard's Tale"""
    num_villagers = int(input())
    num_evenings = int(input())
    bard(num_villagers, num_evenings)

if __name__ == "__main__":
    main()
