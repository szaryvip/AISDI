def merge_sort(list_):
    if list_ == []:
        return []

    numbers = []
    for number in list_:
        numbers.append([number])
    
    while len(numbers) >= 2:
        pair1, pair2 = numbers.pop(0), numbers.pop(0)
        new_pair = []
        while not (len(pair1) == len(pair2) == 0):
            if len(pair1) == 0:
                new_pair += pair2
                break
            elif len(pair2) == 0:
                new_pair += pair1
                break

            if pair1[0] > pair2[0]:
                new_pair.append(pair2.pop(0))
            else:
                new_pair.append(pair1.pop(0))
        numbers.append(new_pair)

    return numbers[0]
