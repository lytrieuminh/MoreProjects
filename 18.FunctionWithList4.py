# Create a function to retrieve certain elements of a list, like the player at index 0.

def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")


top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)
