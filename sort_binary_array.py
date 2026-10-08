def sort_binary_array(arr: list[int]) -> list[int]:
    p1 = 0
    p2 = len(arr) - 1
    while p1 < p2:
        if arr[p1] == 0:
            p1 += 1
            continue
        if arr[p2] == 1:
            p2 -= 1
            continue
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1
    return arr
