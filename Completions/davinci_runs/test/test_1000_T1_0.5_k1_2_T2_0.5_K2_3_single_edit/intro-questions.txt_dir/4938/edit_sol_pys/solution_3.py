

def main():
    max_diff = int(input()) # maximum difference in number of boys and girls
    queue = input() # queue of people
    max_people = 0
    w = 0 # number of girls
    m = 0 # number of boys
    for person in queue:
        if person == 'W': # if girl
            w += 1
        if person == 'M': # if boy
            m += 1
        if abs(w - m) > max_diff: # if difference is greater than the maximum difference
            break
        max_people += 1
    print(max_people)

main()
