# Tables data
tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes',
            'total': [534.50, 20.0, 5]
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


def assign_table(table_number, name, vip_status=False):
    """Assign a table to a guest with optional VIP status.

    Args:
        table_number (int): The table number.
        name (str): The name of the guest.
        vip_status (bool, optional): VIP status of the guest. Defaults to False.
    """
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}


def assign_food_items(table_number, **order_items):
    """Assign food and drinks to a table's order.

    Args:
        table_number (int): The table number.
        **order_items: Arbitrary keyword arguments for food and drinks.
    """

    # Each food item is splited from the food dictionary
    food = order_items.get('food')

    # Each drinks item is splited from the drink dictionary
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks


def calculate_price_per_person(total, tip, split):
    """Calculate the price per person after splitting the bill.

    Args:
        total (float): The total bill amount.
        tip (float): The tip percentage.
        split (int): The number of people to split the bill.
    """
    total_tip = total * (tip / 100)
    split_price = (total + total_tip) / split
    print(split_price)


def remove_guest(table_number):
    """Remove a guest from a table.

    Args:
        table_number (int): The table number.
    """
    tables[table_number]['name'] = None
    tables[table_number]['vip_status'] = None
    tables[table_number]['order'] = {}


def modifty_order(table_number, **order_items):
    """Assign food and drinks to a table's order.

    Args:
        table_number (int): The table number.
        **order_items: Arbitrary keyword arguments for food and drinks.
    """

    # Each food item is splited from the food dictionary
    food = order_items.get('food')

    # Each drinks item is splited from the drink dictionary
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks




# Test code:
table_number = int(input("Please enter a table number:"))
name = str(input("Please enter your name: "))

assign_table(table_number, name)

assign_table(7, 'Taylor', True)
assign_food_items(7,food='Fried Rice, Pizza', drinks = 'Coke')
modifty_order(7, food='Fried Chicken')
print(tables)
