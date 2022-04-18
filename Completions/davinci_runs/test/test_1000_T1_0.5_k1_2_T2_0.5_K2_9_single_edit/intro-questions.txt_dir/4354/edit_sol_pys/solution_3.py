

# input
N, M = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
checkpoints = [list(map(int, input().split())) for _ in range(M)]

for student in students:
    distances = [abs(student[0]-checkpoint[0])+abs(student[1]-checkpoint[1]) for checkpoint in checkpoints]
    print(distances.index(min(distances))+1)
