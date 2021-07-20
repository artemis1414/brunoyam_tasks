def generator_max_number(my_list):
    for i in range(len(my_list)):
        my_list[i] = str(my_list[i])
    my_list.sort(reverse=True)
    max_number = ''
    for i in range(len(my_list)):
        max_digit = '0'
        for j in my_list:
            if str(j)[0] > str(max_digit):
                max_digit = j
        my_list.remove(max_digit)
        max_number += str(max_digit)
    return print(max_number)


example_list = [56, 9, 11, 2, 9, 9, 9, 0, 10, 100]
example_list_2 = [3, 81, 5, 84]
generator_max_number(example_list)
generator_max_number(example_list_2)

