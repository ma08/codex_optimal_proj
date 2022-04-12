

def main(input_file):
    lines = input_file.readlines()
    n, p, m = [int(x) for x in lines[0].strip().split()]
    players = lines[1:1+n]
    scores = lines[1+n:]
    scores = [(name, int(score)) for name, score in [line.strip().split() for line in scores] if name in players]
    scores = sorted(scores, key=lambda x: x[0])
    points = {name: 0 for name in players}
    for name, score in scores:
        points[name] += score
        if points[name] >= p:
            print(name + " wins!")
    if all(points[name] < p for name in points):
        print("No winner!")

if __name__ == "__main__":
    with open("inputs/arcade_basketball.txt", "r") as input_file:
        main(input_file)
