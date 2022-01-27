def quick_sort(list_to_sort):
    if list_to_sort == []:
        return []
    i = 0
    j = len(list_to_sort) - 1
    #here we decide to use iterative or recursive version of quick_sort
    list_to_sort = quick_iterative(list_to_sort, i, j)
    return list_to_sort


def quick_iterative(list_to_sort, i, j):
    stack = [0] * len(list_to_sort)
    top = 0
    stack[top] = i
    top += 1
    stack[top] = j
    while top >= 0:
        j = stack[top]
        top -= 1
        i = stack[top]
        top -= 1
        q = partition(list_to_sort, i, j)
        if q-1 > i:
            top += 1
            stack[top] = i
            top += 1
            stack[top] = q - 1
        if q+1 < j:
            top += 1
            stack[top] = q + 1
            top += 1
            stack[top] = j
    return list_to_sort


def partition(list_to_sort, i, j):
    q = list_to_sort[j]
    possible_place = i - 1
    while i < j:
        if list_to_sort[i] <= q:
            possible_place += 1
            buffor = list_to_sort[i]
            list_to_sort[i] = list_to_sort[possible_place]
            list_to_sort[possible_place] = buffor
        i += 1
    place = possible_place + 1
    buffor = list_to_sort[place]
    list_to_sort[place] = q
    list_to_sort[j] = buffor
    return place


def quick_recursion(list_to_sort, i, j):
    if i < j:
        q = partition(list_to_sort, i, j)
        quick_recursion(list_to_sort, i, q-1)
        quick_recursion(list_to_sort, q+1, j)
    return list_to_sort
