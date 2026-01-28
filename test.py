# test_bug.py
def calculate_price(price):
    # Deliberate infinite recursion or weird logic
    return calculate_price(price);