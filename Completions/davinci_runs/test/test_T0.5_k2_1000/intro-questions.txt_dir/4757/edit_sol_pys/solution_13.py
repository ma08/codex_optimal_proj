
def main():
    """Bard's Tale."""
    num_villagers = int(input()) # number of villagers
    num_evenings = int(input()) # number of evenings
    bard_list = [] # list of villagers who have heard the bard
    bard_list.append(1) # bard is in the list
    for _ in range(num_evenings): # loop through the number of evenings
        num_villagers_present = int(input()) # number of villagers present
        villager_list = [int(i) for i in input().split()] # list of villagers present
        if 1 in villager_list: # if the bard is present
            for i in villager_list: # loop through the villagers present
                if i not in bard_list: # if the villager is not in the bard list
                    bard_list.append(i) # add the villager to the bard list
        else: # if the bard is not present
            for i in villager_list: # loop through the villagers present
                if i not in bard_list: # if the villager is not in the bard list
                    bard_list.append(i) # add the villager to the bard list
    bard_list.sort() # sort the bard list
    for i in bard_list: # loop through the bard list
        print(i) # print the bard list

if __name__ == "__main__":
    main()
