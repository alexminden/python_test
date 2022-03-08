def create_inventory(items):
    """
    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    return {i: items.count(i) for i in items}
def add_items(inventory, items):
    """
 
    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    for x in items:
        if inventory.get(x) is None:
            inventory[x] = 1
        else:
            inventory[x] += 1
    return inventory
def decrement_items(inventory, items):
    """
 
    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    for x in items:
        if inventory[x] > 0:
            inventory[x] -= 1
    return inventory
def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    inventory.pop(item, None)
    return inventory
def list_inventory(inventory):
    """
 
    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [i for i in list(inventory.items()) if i[1] != 0]