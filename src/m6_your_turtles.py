"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Landen Berlin.
"""

########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
red_boy = rg.SimpleTurtle('square')
red_boy.pen = rg.Pen('red',3)
red_boy.speed = 15
size = 100
for k in range (4):
    red_boy.draw_square(size)
    red_boy.pen_up()
    red_boy.right(45)
    red_boy.forward(10)
    red_boy.left(45)
    red_boy.pen_down()
    size = size - 12

blue_boy = rg.TurtleWindow()
blue_boy = rg.SimpleTurtle('circle')
blue_boy.pen = rg.Pen('blue',3)
blue_boy.speed = 5
size = 50
for k in range (10):
    blue_boy.draw_circle(size)
    blue_boy.pen_up()
    blue_boy.left(30)
    blue_boy.forward(20)
    blue_boy.right(30)
    blue_boy.pen_down()
    size = size - 8