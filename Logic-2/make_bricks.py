# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 
# This is a little harder than it looks and can be done without any loops. 
# See also: Introduction to MakeBricks -> https://codingbat.com/doc/practice/makebricks-introduction.html

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

# more conditions to check
# ------------------------
# make_bricks(3, 2, 8) → True
# make_bricks(6, 1, 11) → True
# make_bricks(1, 4, 11) → True
# make_bricks(0, 3, 10) → True 

def make_bricks(small, big, goal):
    # big * 5
    # small * 1
    sum = small + big
    if goal % sum == 0: return True
    else: return False

print(make_bricks(3,2,8))