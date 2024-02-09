original_list=[12,12,12,13,14,15,161,15]
unique_values = list(filter(lambda x: original_list.count(x) == 1, original_list))
print(unique_values)