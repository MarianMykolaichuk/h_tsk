# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.

def count_positives_sum_negatives(arr):
    pos_count, neg_sum = 0, 0
    if arr == []:
        return ([])
    else:
        for number in arr:
            if number > 0:
                pos_count += 1
            elif number < 0:
                neg_sum += number
        return ([pos_count, neg_sum])
    