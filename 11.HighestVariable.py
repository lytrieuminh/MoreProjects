# We'll use a comparison to help us find the highest value and then display it in the console.

user_score = [12, 42, 55, 100, 11, 22]
highest = user_score[0]

for score in user_score:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")
