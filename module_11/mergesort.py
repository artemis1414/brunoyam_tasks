
def merge(beg, end):
    result = []
    i, j = 0, 0
    while i < len(beg) and j < len(end):
        if beg[i] < end[j]:
            result.append(beg[i])
            i += 1
        else:
            result.append(end[j])
            j += 1
    while i < len(beg):
        result.append(beg[i])
        i += 1
    while j < len(end):
        result.append(end[j])
        j += 1
    return result

def merge_sort(list):
    if len(list) < 2:
        return list[:]
    else:
        med = int(len(list) / 2)
        beg = merge_sort(list[:med])
        end = merge_sort(list[med:])
        return merge(beg, end)