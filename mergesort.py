def merge(l, r):

    result = []
    l_index = 0
    r_index = 0

    while l_index < len(l) and r_index < len(r):
        if l[l_index] <= r[r_index]:
            result.append(l[l_index])
            l_index += 1
        else:
            result.append(r[r_index])
            r_index += 1

    while l_index < len(l):
        result.append(l[l_index])
        l_index += 1
    
    while r_index < len(r):
        result.append(r[r_index])
        r_index += 1

    return result

def mergesort_helper(l, r):
    if len(l) == 1 or len(r) == 1: #base case
        return merge(l, r)
    
    else: # inductive step
        
        l1 = l[: int(len(l) / 2)]
        r1 = l[int(len(l) / 2):]
        result_l = mergesort_helper(l1, r1)

        l2 = r[: int(len(r) / 2)]
        r2 = r[int(len(r) / 2):]
        result_r = mergesort_helper(l2, r2)

        return merge(result_l, result_r)

def mergesort(arr):
    mid = (len(arr))//2
    l = arr[:mid]
    r = arr[mid:]
    return mergesort_helper(l, r)

print(mergesort([0, 4, 5, 6]))