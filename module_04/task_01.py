def binary_search(my_list, x):
    start = 0
    last = len(my_list) - 1
    while start <= last:
        middle = int(start + (last - start) / 2)
        if my_list[middle] > x:
            last = middle - 1
        elif my_list[middle] < x:
            start = middle + 1
        elif my_list[middle] == x:
            return middle
    else:
        return None


my_list_number = [x * x for x in range(10)]
print(binary_search(my_list_number, 9))
