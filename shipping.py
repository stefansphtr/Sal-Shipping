# Define the function calculate_ground_shipping_cost

def calculate_ground_shipping_cost(weight):
    """
    Calculate the cost of ground shipping
    based on the package's weight.
    """
    flat_charge = 20
    if weight > 10:
        price_per_pound = 4.75
    elif weight > 6:
        price_per_pound = 4
    elif weight > 2:
        price_per_pound = 3
    else:
        price_per_pound = 1.50
    return round((weight*price_per_pound) + flat_charge, 2)
  
# Define the function drone_shipping_cost

def calculate_drone_shipping_cost(weight):
    """
    Calculate the cost of drone shipping
    based on the package's weight.
    """
    flat_charge = 0
    if weight > 10:
        price_per_pound = 14.25
    elif weight > 6:
        price_per_pound = 12
    elif weight > 2:
        price_per_pound = 9
    else:
        price_per_pound = 4.50
    return round((weight*price_per_pound) + flat_charge, 2)

# Define the function find_cheapest_shipping_method

def find_cheapest_shipping_method(weight):
    """
    Find the cheapest shipping method for a given weight.
    """
    ground_shipping_cost = calculate_ground_shipping_cost(weight)
    ground_shipping_premium_cost = 125
    drone_shipping_cost = calculate_drone_shipping_cost(weight)
    
    cheapest_cost = min(ground_shipping_cost, ground_shipping_premium_cost, drone_shipping_cost)
    
    if cheapest_cost == ground_shipping_cost:
        return f"The cheapest method is Ground Shipping and it will cost $ {ground_shipping_cost}"
    elif cheapest_cost == ground_shipping_premium_cost:
        return f"The cheapest method is Ground Shipping Premium and it will cost $ {ground_shipping_premium_cost}"
    else:
        return f"The cheapest method is Drone Shipping and it will cost $ {drone_shipping_cost}"
    