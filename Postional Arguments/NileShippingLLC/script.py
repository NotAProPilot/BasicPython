"""The back-end file for the script program of Nile Shipping LLC.
"""

import random
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
    """Calculates the shipping cost from one coordinate to another.
    
    Args:
        from_coords (tuple): The (x, y) coordinates of the starting point.
        to_coords (tuple): The (x, y) coordinates of the destination.
        shipping_type (str): The type of shipping (e.g., standard, express).
                             By default, the shipping type is 'Overnight'.
    
    Returns:
        int: The formatted shipping price.
    """
    # Unpacking the tuples into coordinates
    from_lat, from_long = from_coords
    to_lat, to_long = to_coords

    # Calculate the distance using the get_distance function
    distance = get_distance(from_lat, from_long, to_lat, to_long)

    # Get the shipping rate from the SHIPPING_PRICES dictionary
    shipping_rate = SHIPPING_PRICES[shipping_type]

    # Calculate the price
    price = distance * shipping_rate
    
    # Format the price
    final_price = format_price(price)

    # Return the final price
    return final_price

# Test the calculate_shipping_cost function
test_function(calculate_shipping_cost)

def calculate_driver_cost(distance, *drivers):
    """Calculates the salary for drivers.

    Args:
        distance (int): The distance between coordinates.
        *drivers (Driver): The drivers, each driver object should have attributes like speed and salary.
    
    Returns:
        tuple: The price for the cheapest driver and the driver object.
    """
    # Initialize variables for the cheapest driver and price
    cheapest_driver = None
    cheapest_driver_price = None

    # Loop through all drivers to find the cheapest one
    for driver in drivers:
        # Calculate the driving time
        driver_time = distance / driver.speed

        # Calculate the price for each driver
        price_for_driver = driver.salary * driver_time

        # Assign the cheapest driver if the current cheapest driver is None
        if cheapest_driver is None or price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        
    return cheapest_driver_price, cheapest_driver

# Test the calculate_driver_cost function
test_function(calculate_driver_cost)

def calculate_money_made(**trips):
    """A function to calculate the money made for each shipment, I guess.

    Args:
        **tripe: The trip information, in the format of Trip ID: Trip Information.
    """

    # Initialize a counter
    total_money_made = 0

    # Iterate through trip_id and trip information in **trips
    for trip_id, trip in trips.items():
        # Calculate trip revenue:
        trip_revenue = trip.cost - trip.driver.cost

        # Incrementing total money made
        total_money_made = total_money_made + trip_revenue
    
    return total_money_made

test_function(calculate_money_made)


    


