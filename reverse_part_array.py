def reverse_array_helper(arr: list[int], p1: int, p2: int) -> None:
    while p1 < p2:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

def solution(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    k = k % n
    reverse_array_helper(arr, 0, n - 1)
    reverse_array_helper(arr, 0, k - 1)
    reverse_array_helper(arr, k, n - 1)
    return arr
