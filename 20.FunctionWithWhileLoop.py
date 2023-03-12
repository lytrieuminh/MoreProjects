# Functions help us reuse loops by allowing us to change the number of repetitions
# or the list we're iterating through.
# Create a function to call the passengers on board.

def onboard_passenger(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1


onboard_passenger(4)
