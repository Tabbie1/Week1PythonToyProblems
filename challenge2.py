def digit_sum(num):
    #Computing the sum of digits of a number
    return sum(int(digit) for digit in str(num))

def solution(A):
    # setting the maximum sum to -1
    max_sum = -1
    # intialize an object that stores the maximum number with a particular digit sum
    digit_sums = {}
    
    # Iterate through the array A
    for num in A:
        # computing the sum of digits for the current number
        sum_of_digits = digit_sum(num)
        
        # testing to see if the sum of digits has been seen before
        if sum_of_digits in digit_sums:
            # updating the maximum sum if the current number and the previous number with the same digit sum give a larger sum
            max_sum = max(max_sum, digit_sums[sum_of_digits] + num)
            # updating the maximum number with the current digit sum
            digit_sums[sum_of_digits] = max(digit_sums[sum_of_digits], num)
        else:
            # storing the current number as the maximum number with the current digit sum
            digit_sums[sum_of_digits] = num
    
    # to return the maximum sum found, use this;
    return max_sum

# run python3 challenge2.py to confirm the output
print(solution([51, 71, 17, 42]))  # it should output 93
print(solution([42, 33, 60]))      # it should output 102
print(solution([51, 32, 43]))      # it should output -1
