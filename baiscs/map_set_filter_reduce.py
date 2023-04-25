# Pure Functions Extended using Map, Set, Filter and Reduce
# Map
my_list = [1, 2, 3]


def pure_func(item):
    return item * 2


print(list(map(pure_func, my_list)))
print(my_list)

# Filter


def odd_func(item):
    return item % 2 != 0


print(list(filter(odd_func, my_list)))

my_users = ["john""active", ]
