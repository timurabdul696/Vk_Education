def two_sum(nums: list[int], target: int) -> list[int]:
    p1 = 0
    p2 = len(nums) - 1
    while p1 < p2:
        current_sum = nums[p1] + nums[p2]
        if current_sum == target:
            return [p1, p2]
        if current_sum < target:
            p1 += 1
            continue
        p2 -= 1
    return []
