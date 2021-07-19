def check_item_exist(items_list, item):
    if item in items_list:
        return True
    return False


def add_item(items_list, item):
    if not check_item_exist(items_list, item):
        items_list.insert(0, item)
    return items_list


def remove_item(items_list, item):
    if check_item_exist(items_list, item):
        items_list.remove(item)
    return items_list


def rearange_item(items_list, item):
    if check_item_exist(items_list, item):
        items_list.remove(item)
        items_list.append(item)
    return items_list


products = input().split("!")
command_data = input()

while not command_data == "Go Shopping!":
    if len(command_data.split()) == 3:
        products_2 = command_data.split(" ")
        command = products_2[0]
        old_item = products_2[1]
        new_item = products_2[2]
        if command == "Correct":
            if old_item in products:
                index_old_item = products.index(old_item)
                products.remove(old_item)
                products.insert(index_old_item, new_item)
    else:
        command, item = command_data.split()
        if command == "Urgent":
            item = add_item(products, item)
        elif command == "Unnecessary":
            item = remove_item(products, item)
        elif command == "Rearrange":
            item = rearange_item(products, item)
    command_data = input()

for index in range(len(products)):
    if index == len(products) - 1:
        print(f"{products[index]}")
    else:
        print(f"{products[index]},", end=" ")