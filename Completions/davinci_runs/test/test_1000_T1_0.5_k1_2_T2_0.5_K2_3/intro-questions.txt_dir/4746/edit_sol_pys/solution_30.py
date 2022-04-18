

def main():
    capacity, num_stations = map(int, input().split())  # 정원, 정거장 수
    passengers = [0]
    for i in range(num_stations):
        left, entered, waited = map(int, input().split())  # 내린 승객 수, 탄 승객 수, 대기 승객 수
        passengers.append(passengers[-1] + entered - left)
    if passengers[-1] != 0 or max(passengers) > capacity or min(passengers) < 0:  # 승객 수가 정원을 초과하면 불가능
        print("impossible")
    else:
        print("possible")

if __name__ == '__main__':
    main()
