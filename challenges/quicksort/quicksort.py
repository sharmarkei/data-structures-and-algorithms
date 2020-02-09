def partition(lst):
    pivot = lst[-1]
    m = 0

    for i in range(len(lst) - 1):
        if lst[i] <= pivot:
            lst[i], lst[m] = lst[m], lst[i]
            m += 1

        else:
            continue

    lst[m], lst[len(lst)-1] = lst[len(lst)-1], lst[m]

    return m

def quick_sort(lst):
    if len(lst) > 1:
        m = partition(lst)
        return quick_sort(lst[:m]) + quick_sort(lst[m:])

    else:
        return lst
