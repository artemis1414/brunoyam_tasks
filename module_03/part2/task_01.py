my_list = [1, 1, 2, 'hello', 'good', 3, 5, 6, 4, 'hello']
my_list_repeats = []
for element in my_list:
    if my_list.count(element) >= 2 and element not in my_list_repeats:
        my_list_repeats.append(element)
print(my_list_repeats)
