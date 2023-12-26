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
  
