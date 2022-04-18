m = []
n = []
def read_data(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if line:
                line = line.split(',')
                m.append(line[0])
                n.append(line[1])
    return m, n

def write_data(filename, m, n):
    with open(filename, "w") as f:
        for i in range(len(m)):
            f.write(m[i] + "," + n[i] + "\n")
    return

def sort_data(m, n):
    for i in range(len(m)):
        for j in range(len(m) - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
                n[j], n[j + 1] = n[j + 1], n[j]
    return m, n

def main():
    m, n = read_data("data.txt")
    m, n = sort_data(m, n)
    write_data("sorted_data.txt", m, n)

if __name__ == "__main__":
    main()
