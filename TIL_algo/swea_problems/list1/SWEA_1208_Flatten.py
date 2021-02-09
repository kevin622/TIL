for test_case in range(1, 11):
    dump = int(input())
    box_heights = list(map(lambda x: int(x) - 1, input().split()))
    # Now, all heights are between 0 and 99
    # similar to index

    count_list = [0] * 100
    for height in box_heights:
        count_list[height] += 1

    while dump:
        for idx in range(len(count_list)):
            if count_list[idx]:
                count_list[idx] -= 1
                count_list[idx + 1] += 1
                break
        for idx in range(len(count_list) - 1, 0, -1):
            if count_list[idx]:
                count_list[idx] -= 1
                count_list[idx - 1] += 1
                break
        dump -= 1

    answer = [0, 0]
    for idx in range(len(count_list)):
        if count_list[idx]:
            answer[0] = idx
            break
    for idx in range(len(count_list) - 1, 0, -1):
        if count_list[idx]:
            answer[1] = idx
            break

    print('#{} {}'.format(test_case, answer[1] - answer[0]))