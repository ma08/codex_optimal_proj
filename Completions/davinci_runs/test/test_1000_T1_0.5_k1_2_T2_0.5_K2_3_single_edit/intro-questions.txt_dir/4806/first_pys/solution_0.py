

def main():
    moves = input()
    result = ""
    i = 0
    while i < len(moves):
        if i + 2 < len(moves) and moves[i] == moves[i+1] == moves[i+2]:
            result += "C"
            i += 3
        elif moves[i] == "R":
            result += "S"
            i += 1
        elif moves[i] == "B":
            result += "K"
            i += 1
        elif moves[i] == "L":
            result += "H"
            i += 1
    print(result)

main()