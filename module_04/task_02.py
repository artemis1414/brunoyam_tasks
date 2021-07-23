def Insertion_sort(my_list):
    for index in range(1, len(my_list)):
        current_element = my_list[index]
        previous_index = index - 1
        while previous_index >= 0 and my_list[previous_index] > current_element:
            my_list[previous_index + 1] = my_list[previous_index]
            my_list[previous_index] = current_element
            previous_index -= 1
    return my_list


list = [456, 700, 200, 100, 594, 563, 1038, 32, 459, 67430, 5764, 863, 7548, 1234, 2947, 212, 54, 723, 2124]

print(Insertion_sort(list))