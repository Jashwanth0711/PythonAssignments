numbers = [1,2,3,4,0,0,1,2,3,4,0,0,0,6]
non_zero = []  
zero_list = []
for n in numbers:
    if n == 0:
        zero_list.append(n)
    else:
        non_zero.append(n)  
result = non_zero + zero_list

print(result)


# lst = [1,2,3,4,0,0,1,2,3,4,0,0,0,6]
# lst2 = []

# for number in lst:
#     if number != 0:
#         lst2.append(number)
# for number in lst:
#     if number == 0:
#         lst2.append(number)

# print(lst2)