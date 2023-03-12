# Create a function to count down for an action.

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")


do_countdown(3)
