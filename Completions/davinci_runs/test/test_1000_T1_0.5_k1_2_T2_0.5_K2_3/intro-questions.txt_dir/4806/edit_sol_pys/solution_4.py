

def main():
    moves = input().upper()
    result = ""
    i = 0
    while i < len(moves):
        if i + 2 < len(moves) and moves[i] == moves[i+1] == moves[i+2]:
            result += "C"
            i += 3
        elif moves[i] == "R" or moves[i] == "P" or moves[i] == "S":
            result += "S"
            i += 2
        elif moves[i] == "B" or moves[i] == "K" or moves[i] == "G":
            result += "K"
            i += 2
        elif moves[i] == "L" or moves[i] == "H" or moves[i] == "W":
            result += "H"
            i += 1
    print(result)

main()
