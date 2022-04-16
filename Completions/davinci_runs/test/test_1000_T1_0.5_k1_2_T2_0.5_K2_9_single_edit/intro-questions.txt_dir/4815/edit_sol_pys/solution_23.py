

def main(input_file):
    lines = input_file.readlines()
    n, p, m = map(int, lines[0].strip().split())
    players = [line.strip() for line in lines[1:1+n]]
    scores = lines[1+n:1+n+m]
    scores = [line.strip().split() for line in scores]
    scores = [(name, int(score)) for name, score in scores]
    points = {name: 0 for name in players}
    for name, score in scores:
        points[name] += score
        if points[name] >= p and all(points[name] < p for name in points if name != name):
            print(name + " wins!")
    if all(points[name] < p for name in points):
        print("No winner!")

if __name__ == "__main__":
    with open("inputs/arcade_basketball.txt", "r") as input_file:
        main(input_file)
