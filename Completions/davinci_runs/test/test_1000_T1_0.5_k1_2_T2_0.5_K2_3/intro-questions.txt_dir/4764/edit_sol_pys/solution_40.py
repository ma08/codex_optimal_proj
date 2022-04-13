

def main():
    n, h, v = [int(i) for i in input().split()]  # n = nombre de cookies, h = hauteur, v = largeur
    print(h * v * 4)  # (h * v) * 4 = surface du papier

if __name__ == '__main__':
    main()
