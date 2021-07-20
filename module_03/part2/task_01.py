my_list = [1, 1, 2, 'hello', 'good', 3, 5, 6, 4, 'hello']
my_list_repeats = []
for i in my_list:
    count = 0
    for j in range(len(my_list)):
        if my_list[j] == i:
            count += 1
    if count > 1:
        my_list_repeats.append(i)
print(my_list_repeats)
