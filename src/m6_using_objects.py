"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Nathan Pryor.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(500,500)
    center_point1 = rg.Point(50, 50)
    radius1 = 20
    circle1 = rg.Circle(center_point1, radius1)
    circle1.fill_color = 'blue'
    circle1.attach_to(window)

    center_point2 = rg.Point(250, 300)
    radius2 = 70
    circle2 = rg.Circle(center_point2, radius2)
    circle2.attach_to(window)

    window.render()

    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow(500, 500)
    center_point = rg.Point(70, 200)
    radius = 20
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window)
    circle.outline_thickness = 1
    pt1 = rg.Point(175, 150)
    pt2 = rg.Point(300, 100)
    rectangle = rg.Rectangle(pt1, pt2)
    rectangle.attach_to(window)
    rectangle.outline_thickness = 1

    print('1')
    print('blue')
    print('Point(70.0, 200.0)')
    print('70.0')
    print('200.0')
    print('1')
    print('None')
    print(rectangle.get_center())
    print('237.5')
    print('125.0')

    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    window = rg.RoseWindow(500, 500)
    pt1a = rg.Point(150, 150)
    pt2a = rg.Point(50, 50)
    line1 = rg.Line(pt1a,pt2a)
    line1.attach_to(window)
    pt1b = rg.Point(400, 450)
    pt2b = rg.Point(260, 260)
    line2 = rg.Line(pt1b,pt2b)
    line2.thickness = 10
    line2.attach_to(window)

    print(line2.get_midpoint())
    print('330.0')
    print('355.0')

    window.render()

    window.close_on_mouse_click()

    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
