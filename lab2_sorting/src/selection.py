def min(list_, start_index=0):
    minimum = list_[start_index]
    for element in list_[start_index:]:
        if element < minimum:
            minimum = element
    return minimum


def selection_sort(list_):
    for index in range(len(list_)):
        minimum = min(list_, index)
        minimum_index = len(list_) - 1 - list_[::-1].index(minimum)
        list_[index], list_[minimum_index] = list_[minimum_index], list_[index]
    return list_

# print(selection_sort([5,3,8,4,8,4,90,3,0,1,5]))
