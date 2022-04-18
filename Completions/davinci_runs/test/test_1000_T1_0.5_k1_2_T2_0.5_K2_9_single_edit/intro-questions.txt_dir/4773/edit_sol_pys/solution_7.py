

def main():
    route = input()
    route = list(route)
    route.reverse()
    curr_move = route.pop()
    curr_count = 1
    while route:
        next_move = route.pop()
        if next_move == curr_move:
            curr_count += 1
        else:
            curr_move = next_move
            curr_count = 1
    print(curr_count + 1)

main()
