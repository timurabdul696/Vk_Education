def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    merged_array = []
    p1 = 0
    p2 = 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            merged_array.append(arr1[p1])
            p1 += 1
            continue
        merged_array.append(arr2[p2])
        p2 += 1
    merged_array.extend(arr1[p1:])
    merged_array.extend(arr2[p2:])
    return merged_array
