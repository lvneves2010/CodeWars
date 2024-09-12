def max_sequence(arr):
    result = 0
    if len(arr) > 0:
        if min(arr) > -1:
            result = sum(int(num) for num in arr)
        elif max(arr) < 0:
            result = 0
        else:
            result = max_sum_sublist(arr)
            
    return result
    pass
                    
def max_sum_sublist(lst):
    max_sum = float('-inf')
    start_idx = 0
    end_idx = 0
    current_sum = 0
    current_start_idx = 0

    for i, num in enumerate(lst):
        current_sum += num
        if current_sum < 0:
            current_sum = 0
            current_start_idx = i + 1
        elif current_sum > max_sum:
            max_sum = current_sum
            start_idx = current_start_idx
            end_idx = i

    return max_sum