# 3
# 9
# 7 4 2 0 0 6 0 7 0
# 9
# 7 4 2 0 0 6 7 7 0
# 20
# 52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

# 7
# 6
# 13

# Getting the input file
import sys
sys.stdin = open("input.txt", "r")

# The number of all the test cases
all_case = int(input())


for test_case_num in range(all_case):
    # Initialize
    answer = 0
    # The size of the box
    num_of_input = int(input())
    # Each box piles(tower?)
    boxes = list(map(int, input().split()))

    for idx in range(num_of_input - 1):
        count = 0
        # Getting the count of all the boxes that have higher height
        # than the box that is being checked
        # for only those on the right of the box
        for i in map(lambda box: boxes[idx] <= box, boxes[idx + 1:]):
            count += i
        # The strongest drop of the current pile of boxes
        fall = num_of_input - 1 - idx - count

        # If the drop is stronger than the previous strongest,
        # update the value
        if fall > answer:
            answer = fall
    print(answer)
