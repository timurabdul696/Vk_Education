def min_sub_array(nums: list[int], target: int) -> int:
    min_len = float('inf')
    p1 = 0
    cur_sum = 0
    p2 = 0
    while p2 < len(nums):
        cur_sum += nums[p2]
        while cur_sum >= target:
            window_size = p2 - p1 + 1
            if window_size < min_len:
                min_len = window_size
            cur_sum -= nums[p1]
            p1 += 1
        p2 += 1
    return min_len if min_len != float('inf') else 0
