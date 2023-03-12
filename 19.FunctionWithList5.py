# Create a function to update a list.

def update_first_place(leaderboard, player):
    leaderboard[0] = player
    return leaderboard


leaderboard = ["Jay", "Meg", "Cy"]
leaderboard = update_first_place(leaderboard, "Lena")
print(leaderboard)
