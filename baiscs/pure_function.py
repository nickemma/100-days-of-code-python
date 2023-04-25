# Pure Function

def pure_func(li):
    new_list = []
    for item in li:
        new_list.append(item*2)

    return new_list


print(pure_func([1, 2, 3]))
