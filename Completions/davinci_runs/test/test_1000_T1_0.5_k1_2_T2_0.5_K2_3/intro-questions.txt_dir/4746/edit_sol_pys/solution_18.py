
def main():
    capacity, num_stations = map(int, input().split())
    passengers = [0]
    for i in range(num_stations):
        left, entered, waited = map(int, input().split())  # 이미 있던 승객 수, 탄 승객 수, 대기 승객 수
        passengers.append(passengers[-1] + entered - left)
    if passengers[-1] != 0 or max(passengers) > capacity or min(passengers) < 0 or num_stations == 1:
        print("impossible")
    else:
        print("possible")

if __name__ == '__main__':
    main()
