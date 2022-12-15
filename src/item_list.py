item_names = []

with open("src/all_stuff.feda", "r") as file:
    for line in file:
        item_names.append(line.strip())


def add_item(item_name):
    item_names.append(item_name)
    with open("src/all_stuff.feda", "w") as file:
        for item in item_names:
            file.write(item + "\n")


def delete_item(item_id):
    item_names.pop(item_id)
    with open("src/all_stuff.feda", "w") as file:
        for item in item_names:
            file.write(item + "\n")


if __name__ == '__main__':
    delete_item(5)
