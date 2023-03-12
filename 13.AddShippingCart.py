# Create a function to make a decision, like adding shipping cost or not,
# but based on if the cart has a certain value or not.

def add_shipping(cart):
    if cart > 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")


add_shipping(45)
add_shipping(200)
