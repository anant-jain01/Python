def flashsort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    m = int(n * 0.43) 
    if m < 1:
        m = 1
    buckets = [0] * m
    for value in arr:
        index = int((value - min_val) / (max_val - min_val + 1e-9) * (m - 1))
        buckets[index] += 1
    for i in range(1, m):
        buckets[i] += buckets[i - 1]
    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = arr[i]
        index = int((value - min_val) / (max_val - min_val + 1e-9) * (m - 1))
        output[buckets[index] - 1] = value
        buckets[index] -= 1
    return output
