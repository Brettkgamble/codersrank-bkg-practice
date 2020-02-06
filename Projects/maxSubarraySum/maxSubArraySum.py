# for each element in array
# loop through and sum each element moving through the array
# one element at a time
def max_sequence(arr):
    if not len(arr) == 0:
        sorted_arr = sorted(arr, reverse=True)
        # If first and last element of sorted array > 0, then all positive
        # return sum
        if sorted_arr[0] > 0:
            if sorted_arr[-1] > 0:
                s = 0
                for n in arr:
                    s += n
                return s
        # if 1st element of sorted array is negative, then all are negative
        # return 0
        else:
            return 0
        # If here then previous conditions are not met
        # find largest sum
        sum = 0
        roll_sum = arr[0]
        for i in range(0, len(arr)):
            for n in range(i, len(arr)):
                sum += arr[n]
                if sum >= roll_sum:
                    roll_sum = sum
            sum = 0
        return roll_sum
    else:
        return 0

print(max_sequence([]))
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([1, 2, 3, 4, 5, 6]))
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))