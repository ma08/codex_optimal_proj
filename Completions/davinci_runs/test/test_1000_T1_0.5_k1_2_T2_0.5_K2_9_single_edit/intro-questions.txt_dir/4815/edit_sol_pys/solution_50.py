

def main(input_file):
    lines = input_file.readlines()
    n, p, m = [int(x) for x in lines[0].strip().split()]
    players = [line.strip() for line in lines[1:1+n]]
    scores = [line.strip().split() for line in lines[1+n:]]
    scores = sorted([(name, int(score)) for name, score in scores], key=lambda x: x[0])
    points = {name: 0 for name in players if name}
    for name, score in [x for x in scores if x[0]]:
        points[name] += score
        if points[name] >= p:
            print(name + " wins!")
    if all(points[name] < p for name in points):
        print("No winner!")

if __name__ == "__main__":
    with open("inputs/arcade_basketball.txt", "r") as input_file:
        main(input_file)
