def even_first(arr: list[int]) -> list[int]:
    p1 = 0
    p2 = 0
    while p2 < len(arr):
        if arr[p2] % 2 == 0:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1 += 1
            p2 += 1
            continue
        p2 += 1
    return arr
