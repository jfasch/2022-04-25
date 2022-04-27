input_list = [2, 3, 1, 10, 3, 3, 1, 10, 5, 2]

output_list = []
have = set()

for num in input_list:
    if num not in have:     # <---- HIER!!! SPEEEEEEED!!
        output_list.append(num)
        have.add(num)

for num in output_list:
    print(num)
