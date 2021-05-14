from Inventory import *
if __name__ == "__main__":
    item_type = "PC"
    inv = Inventory()
    inv.lock(item_type)
    try:
        num_left = inv.purchase(item_type)
    except ItemNotFound:
        print("Sorry, we don't sell {}".format(item_type))
    except OutOfStock:
        print("Sorry, that item is out of stock.")
    except ItemNotLocked:
        print("the item is not locked so you can`t continue!")
    else:
        print("Purchase complete. There are ""{} {}s left".format(num_left, item_type))
    finally:
        inv.unlock(item_type)
