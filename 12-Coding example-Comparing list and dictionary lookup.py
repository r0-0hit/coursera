import timeit

# List lookup
list_data = list(range(100000))
lookup_value = 99999
list_time = timeit.timeit(lambda: lookup_value in list_data, number=10000)
list_index_time = timeit.timeit(lambda: list_data.index(lookup_value), number=10000)

# Dictionary lookup
dict_data = {i: i for i in range(100000)}
dict_time = timeit.timeit(lambda: lookup_value in dict_data, number=10000)

print("List lookup time:", list_time)
print("List lookup time:", list_index_time)
print("Dictionary lookup time:", dict_time)
