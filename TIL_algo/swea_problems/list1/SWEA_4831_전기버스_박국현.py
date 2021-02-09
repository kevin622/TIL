T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    # Signing all the bus stops with charge station
    bus_stops = [0] * (N + 1)
    station_idx = 0
    for idx in range(len(bus_stops)):
        if idx == station[station_idx]:
            bus_stops[idx] = 1
            station_idx += 1
            if station_idx == len(station):
                break

    bus_stops = list(enumerate(bus_stops))
    curr_idx = 0
    answer = 0

    while True:
        if curr_idx + K >= N:
            break

        for idx in range(curr_idx + K, curr_idx, -1):
            if bus_stops[idx][1] == 1:
                curr_idx = idx
                answer += 1
                break
        else:
            answer = 0
            break
    print('#{} {}'.format(test_case, answer))