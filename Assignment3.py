items = input("Enter all types of data separated by commas: ")
items_list = [x.strip() for x in items.split(",")]
print(items_list)
result = []

for data in items_list:
    if data == "True":
        result.append(True)
    elif data == "False":
        result.append(False)
    elif "." in data:
        result.append(float(data))
    else:
        result.append(int(data))

print(result)
