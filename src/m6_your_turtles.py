"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Emily Wilcox.
"""
###############################################################################
# done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# done: 2.
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
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('pink', 15)
red_turtle.speed = 15

size = 100

for k in range(10):
    red_turtle.draw_regular_polygon(5 , 75)


    red_turtle.pen_up()
    red_turtle.left(16)
    red_turtle.forward(25)
    red_turtle.left(45)
    red_turtle.left(19)
    red_turtle.backward(60)


    red_turtle.pen_down()
    size = size - 20

window.close_on_mouse_click()