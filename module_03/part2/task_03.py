d = {'name1': 'id1', 'name2': 'id2', 'name3': 'id3'}
d_inversion = {}
for i, j in d.items():
    d_inversion.setdefault(j, i)
d = d_inversion
print(d)
