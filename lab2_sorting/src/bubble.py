def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort)-1):
        for j in range(len(list_to_sort)-1-i):
            if list_to_sort[j] > list_to_sort[j+1]:
                buffor = list_to_sort[j+1]
                list_to_sort[j+1] = list_to_sort[j]
                list_to_sort[j] = buffor
    return list_to_sort
