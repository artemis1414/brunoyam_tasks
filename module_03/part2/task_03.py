d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3', 'a': 1, 'b': 1, 'c': 1}
d_inversion = {}
for i, j in d.items():
    if j in d_inversion:
        d_inversion[j].append(i)
    else:
        d_inversion.setdefault(j, [i])
d = d_inversion
print(d)





