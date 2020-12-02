# The only two built in functions for Reeborg are move() and turn_left(). We need our own turn_right()
def turn_right():
    for i in range(3):
        turn_left()

# This counter is needed if Reeborg starts in a position where it can get stuck in a loop based on open map squares
right_turns = 0        
        
while not at_goal():
    if right_is_clear() and right_turns < 4:
        turn_right()
        move()
        right_turns += 1
    elif front_is_clear():
        move()
        right_turns = 0
    else:
        turn_left()
        right_turns = 0