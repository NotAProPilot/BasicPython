"""The testing file for the script program of Nile Shipping LLC.
"""

def test_function(fn):
    """Calls the appropriate test function based on the function name.

    Args:
        fn (function): The function to be tested.
    """
    if fn.__name__ == "calculate_shipping_cost":
        test_shipping(fn)
    elif fn.__name__ == "calculate_driver_cost":
        test_driver(fn)
    elif fn.__name__ == "calculate_money_made":
        test_money(fn)


def test_shipping(f):
    """Tests the calculate_shipping_cost function.

    Args:
        f (function): The calculate_shipping_cost function.
    """
    try:
        costs = f((0, 0), (1, 1))
    except TypeError:
        print("\033[91mcalculate_shipping_cost() did not provide default argument for shipping_type\033[0m")
        return
    if not isinstance(costs, str):
        print("\033[91mcalculate_shipping_cost() did not format the result in a string\033[0m")
        return
    if costs != "$1.04":
        print("\033[91mcalculate_shipping_cost((0, 0), (1, 1)) returned {}. Expected result is {}\033[0m".format(costs, "$1.04"))
        return
    print("\033[92mOK! calculate_shipping_cost() passes tests\033[0m")


class Driver:
    """Represents a driver.

    Attributes:
        speed (int): The speed of the driver.
        salary (int): The salary of the driver.
    """

    def __init__(self, speed, salary):
        self.speed = speed
        self.salary = salary

    def __repr__(self):
        return "Nile Driver speed {} salary {}".format(self.speed, self.salary)


driver1 = Driver(4, 10)
driver2 = Driver(7, 20)


def test_driver(f):
    """Tests the calculate_driver_cost function.

    Args:
        f (function): The calculate_driver_cost function.
    """
    try:
        price, driver = f(80, driver1, driver2)
    except TypeError:
        print("\033[91mcalculate_driver_cost() doesn't expect multiple driver arguments\033[0m")
        return
    if not isinstance(driver, Driver):
        print("\033[91mcalculate_driver_cost() did not return driver\033[0m")
        return
    if price != 200:
        print("\033[91mcalculate_driver_cost() did not provide correct final price (expected {}, received {})\033[0m".format(200, price))
        return
    if driver is not driver1:
        print("\033[91mcalculate_driver_cost() did not provide least expensive driver\033[0m")
        return
    print("\033[92mOK! calculate_driver_cost() passes tests\033[0m")


class Trip:
    """Represents a trip.

    Attributes:
        cost (int): The cost of the trip.
        driver (Driver): The driver for the trip.
        driver_cost (int): The cost associated with the driver.
    """

    def __init__(self, cost, driver, driver_cost):
        self.cost = cost
        driver.cost = driver_cost
        self.driver = driver


trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)


def test_money(f):
    """Tests the calculate_money_made function.

    Args:
        f (function): The calculate_money_made function.
    """
    try:
        money = f(UEXODI=trip1, DEFZXIE=trip2)
    except TypeError:
        print("\033[91mcalculate_money_made() doesn't expect multiple trip keyword arguments\033[0m")
        return
    if not isinstance(money, (int, float)):
        print("\033[91mcalculate_money_made() did not return a number\033[0m")
        return
    if money != 445:
        print("\033[91mcalculate_money_made() did not provide correct final price (expected {}, received {})\033[0m".format(445, money))
        return
    print("\033[92mOK! calculate_money_made() passes tests\033[0m")
