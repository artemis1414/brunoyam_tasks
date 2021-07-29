d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3', 'a': 1, 'b': 1, 'c': 1}
d_inversion = {}
for key, value in d.items():
    if value in d_inversion:
        d_inversion[value].append(key)
    else:
        d_inversion[value] = [key]
d = d_inversion
print(d)





