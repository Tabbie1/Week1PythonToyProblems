def solution(A):
    # to compute the total number of bricks
    total_bricks = sum(A)
    # to compute the target number of bricks per box
    target_bricks = 10 * len(A)
    
    # testing to see how possible it is to achieve the target
    if total_bricks < target_bricks or total_bricks % len(A) != 0:
        return -1
    
    # define and initialize the number of moves
    moves = 0
    # computing the number of bricks per box
    bricks_per_box = total_bricks // len(A)
    
    # Iterate through the boxes to balance the bricks
    for i in range(1, len(A)):
        # computing the difference between the current box's bricks and the target
        diff = A[i] - bricks_per_box
        # modify the number of bricks in the current box
        A[i] -= diff
        # move the number of extra or missing bricks to the next box
        A[i - 1] += diff
        # register the total number of moves made
        moves += abs(diff)
    
    # use return to output the total number of moves made
    return moves

#  run python3 challenge1.py to confirm the output
print(solution([7, 15, 10, 8]))  # the output will be 7
print(solution([11, 10, 8, 12, 8, 10, 11]))  # the output will be 6
print(solution([7, 14, 10]))  # the output will be -1
