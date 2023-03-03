# Let's code a program that keeps track of a person's savings
# and updates if the person has made purchases or earned money.

goal = 150
savings = 70

print(f"You're ${goal - savings} away from your goal")

earned = 75
savings += earned
print(f"You're ${goal - savings} away from your goal")

spent = 25
savings -= spent
print(f"You're ${goal - savings} away from your goal")
