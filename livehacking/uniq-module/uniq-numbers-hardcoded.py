import uniq


input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]

unique_list = uniq.unique(input_list, [5, 2, 1, 666])

for num in unique_list:
    print(num)


