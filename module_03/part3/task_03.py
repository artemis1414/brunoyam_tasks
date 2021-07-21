def generator_max_number(my_list):
    my_list = [str(i) for i in my_list]
    my_list.sort(reverse=True)
    max_number = "".join(my_list)
    return print(max_number)

# def generator_max_number_2(my_list):
#     max_number = ''
#     for i in range(len(my_list)):
#         my_list[i] = str(my_list[i])
#     max_number = [i for i in my_list]
#     return print(max_number)


example_list = [56, 9, 11, 2, 9, 9, 9, 0, 10, 100]
example_list_2 = [3, 81, 5, 84]
generator_max_number(example_list)
generator_max_number(example_list_2)

