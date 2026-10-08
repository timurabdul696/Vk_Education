def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    p1 = len(arr1) - len(arr2) - 1
    p2 = len(arr2) - 1
    p3 = len(arr1) - 1
    while p2 >= 0:
        if p1 >= 0 and arr1[p1] > arr2[p2]:
            arr1[p3] = arr1[p1]
            p1 -= 1
        else:
            arr1[p3] = arr2[p2]
            p2 -= 1
        p3 -= 1
    return arr1
