# 21 Sticks
# The Game:
# In this game, there are 21 sticks lying in a pile.
# Players take turns taking 1, 2, or 3 sticks. 
# The last person to take a stick wins. Like this:

# 21 sticks
# Bob takes 2

# 19 sticks
# Alice takes 3

# 16 sticks
# Bob takes 3

# 13 sticks
# Alice takes 1

# 12 sticks
# Bob takes 2

# 10 sticks
# Alice takes 2

# 8 sticks
# Bob takes 3

# 5 sticks
# Alice takes 3

# 2 sticks
# Bob takes 2
# Bob wins!
# Your task:
# Create a robot that will always win the game. Your robot will always go first. The function should take an integer and returns 1, 2, or 3.

# Example:

# make_move(2) == 2
# # => 1


def make_move(sticks):
    sticks = (20-sticks)%4
    if sticks == 1:
        sticks = 3
    elif sticks == 2:
        sticks == 2
    elif sticks == 3:
        sticks = 1
    return sticks

    # test.assert_equals(make_move(3), 3, 'You robot did not take 3 to win')