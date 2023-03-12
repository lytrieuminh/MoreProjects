# Everyday at noon, we'll add the newest humidity value to the beginning of the list,
# and remove the oldest value.

humidity_level = [87, 83, 89, 88, 87]

humidity_level.insert(0, 90)
humidity_level.pop()
print(humidity_level)
