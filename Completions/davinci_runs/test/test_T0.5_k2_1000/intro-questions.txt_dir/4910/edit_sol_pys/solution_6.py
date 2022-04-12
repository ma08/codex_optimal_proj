"""
File: file.py
Author: setcain
Email: setcain@email.com
Github: https://github.com/setcain
Description: 
"""



def main():
    """
    Main function
    """
    num_costumes = int(input()) # number of costumes
    costumes = [] # list of costumes
    for _ in range(num_costumes): # loop through number of costumes
        costumes.append(input()) # add costumes to list
    costume_set = set(costumes) # set of costumes
    costume_counts = [costumes.count(costume) for costume in costume_set] # list of costume counts
    max_count = max(costume_counts) # max costume count
    winners = [costume for costume, count in zip(costume_set, costume_counts) if count == max_count] # list of winners
    print('\n'.join(sorted(winners))) # print winners

if __name__ == "__main__":
    main()
