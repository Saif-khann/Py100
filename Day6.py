'''
🐍 (Py100: 100 Days of Python Challenge)
Author: Saif Khan
-----------------------------------
Day 6: Maze Challenge with Reeborg
-----------------------------------
Reeborg is lost in a dark maze, and the battery in its flashlight has run out.
Our goal is to guide Reeborg from its starting position to the exit (flag) using predefined functions.
The task is to make Reeborg follow the right edge of the maze by checking for walls and open paths. 
Turning right if possible, moving forward if possible, or turning left as a last resort.

The website provides some predefined functions like:
- move(): Moves Reeborg one step forward.
- turn_left(): Rotates Reeborg 90 degrees to the left.
- right_is_clear(), front_is_clear(), at_goal(): Conditions that help us navigate.

The challenge here is to use logical conditions and loops to solve the maze. However, there are
scenarios where the bot might enter an infinite loop (e.g., turning right continuously in an open area).
This is an intermediate issue, which we will debug later, as advised by the course instructor.

Please note: This code only works within the Reeborg.ca environment. It won't run in other IDEs or Python environments
as the maze environment and functions are exclusive to that website.
'''

def turn_right():
    # Since Reeborg only has a turn_left() function, 
    # we need to define our own function to turn right by rotating three times to the left.
    turn_left()
    turn_left()
    turn_left()

# The main loop where Reeborg moves towards the goal
while not at_goal():  # The loop continues until Reeborg reaches the goal.
    
    # Check if Reeborg can turn right and move in that direction.
    if right_is_clear():
        turn_right()
        move()
    
    # If right is not clear, check if the front is clear and move forward.
    elif front_is_clear():
        move()
    
    # If neither right nor front is clear, Reeborg must turn left.
    else:
        turn_left()

# Note: Some edge cases can cause Reeborg to loop infinitely, but these will be addressed after Day 15.
# 📝 Future Debug: Fix infinite loop cases after Day 15



