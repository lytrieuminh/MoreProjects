# Let's code an app that keeps track of tennis games that have been played
# and if it reaches 6 games, then they've finished the set.

games = 0
set_finished = False

while set_finished == False:
    games += 1
    print(f"Games played: {games}")
    if games == 6:
        set_finished = True
print("Finished the set!")
