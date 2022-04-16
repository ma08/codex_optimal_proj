

def find_max_team_size(skills):
    pass

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        skills = list(map(int, input().split()))
        print(find_max_team_size(skills))
