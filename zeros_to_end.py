def zeros_to_end(nums: list[int]) -> list[int]:
    p1 = 0
    p2 = 0
    while p2 < len(nums):
        if nums[p2] != 0:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1
            p2 += 1
            continue
        p2 += 1
    return nums

print(zeros_to_end([0, 0, 1, 0, 3, 12]))
print(zeros_to_end([0, 33, 57, 88, 60, 0, 0, 80, 99]))
print(zeros_to_end([0, 0, 0, 18, 16, 0, 0, 77, 99]))
