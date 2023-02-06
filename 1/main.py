import random

n = int(input("Enter number of items:"))
x = int(input("Enter number for search:"))
my_list = list()
for _ in range(n):
    my_list.append(random.randint(1, 101))
print(f'List : {my_list}')

closest_number = my_list[0]
differance = abs(x - closest_number)
quantity = my_list.count(x)
curr_diff = differance
if quantity == 0:
    for item in my_list:
        curr_diff = abs(x - item)
        if curr_diff < differance:
            differance = curr_diff
            closest_number = item

    print(f'Closest number in list {closest_number}')
else:
    print(f'The count of {x} is {quantity}')
