def generator_max_number(my_list):
    str_number = sorted([str(i) for i in my_list], reverse=True)
    max_number = "".join(str_number)
    print(max_number)


example_list = [56, 9, 11, 2, 9, 9, 9, 0, 10, 100]
example_list_2 = [3, 81, 5, 84]
generator_max_number(example_list)
generator_max_number(example_list_2)

