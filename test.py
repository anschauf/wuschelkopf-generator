from itertools import repeat
given_value =4
new_list=[]
new_list.extend(repeat(given_value,5))


direct_list = list(repeat(4, 2)) +  list(repeat(8, 4))
print(new_list)

print(direct_list)
print(sum(direct_list))


test_values = list(repeat(12, 15)) + list(repeat(12, 15)) + list(repeat(15, 4))

#
print(sum(test_values))