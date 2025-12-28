# Group Name: DAN/EXT 01
# Group Members: 4
# Member 1: Md Hasibul Raihan - S397592
# Member 2: Tanisa Sanam Vabna - S397593
# Member 3: JESHIKA SAPKOTA - S399269
# Member 4: LADDAPORN DAWSON - S382273

# Create a program that uses a recursive function to generate a geometric pattern using Python's turtle graphics. 

import turtle # import: Python keyword to bring in external modules. # turtle: Used for drawing graphics with a virtual pen.

def draw_fractal_edge(t, length, depth, inward=True): # keyword arguments (**kwargs, *args)

    """
    Draw one fractal edge using Koch-like rules.

    t       : turtle object
    length  : length of the current edge
    depth   : recursion depth
    inward  : if True, the triangle indents inward;
              if False, it bulges outward
    """
    if depth == 0: #This is the base case of the recursion.
        # Base case: draw a straight line
        t.forward(length)
        return #Stops the function here. 

    # Recursive case: apply the Koch-like rules 
    segment = length / 3.0

    # First third: recursively draw a smaller fractal of length (segment) and depth - 1
    draw_fractal_edge(t, segment, depth - 1, inward)

    # Turn to create triangle indentation
    if inward:
        t.right(60)   #Turn right 60° so the triangle goes inward.
    else:
        t.left(60)    #Turn left 60° so the triangle bulges out.

    # Second third: draws the first side of the small triangle, again recursively

    draw_fractal_edge(t, segment, depth - 1, inward)

    # Turn across the top of the triangle
    if inward:
        t.left(120)
    else:
        t.right(120)

    # Third third: draws the second side of the small triangle
    draw_fractal_edge(t, segment, depth - 1, inward)

    # Turn back to original direction
    if inward:
        t.right(60)
    else:
        t.left(60)

    # Last third: draws the final part of the edge.

    draw_fractal_edge(t, segment, depth - 1, inward)


def draw_regular_polygon(t, sides, side_length): # keyword arguments (**kwargs, *args)
    """
    Position the turtle to draw a regular polygon, then draw it
    with straight edges (no recursion here, just for reference
    or depth=0 behavior).
    """
    angle = 360.0 / sides    #Turn angle at each corner.
    for _ in range(sides):   #Repeat for each side
        t.forward(side_length) #Move forward by side_length.
        t.right(angle)         #Turn right by angle.


def draw_fractal_polygon(t, sides, side_length, depth, inward=True): # keyword arguments (**kwargs, *args)
    """
    Draw a fractal pattern on all sides of a regular polygon.

    t           : turtle object
    sides       : number of sides of the starting polygon
    side_length : length of each side in pixels
    depth       : recursion depth
    inward      : True for indentation, False for outward bumps
    """
    angle = 360.0 / sides    #Same idea as before, the turning angle at each vertex.

    for _ in range(sides):   #For each side of the polygon
        draw_fractal_edge(t, side_length, depth, inward)  #Call draw_fractal_edge instead of straight line.
        t.right(angle)  #Then turn by angle to face the next side.


def main():
    # --- User input ---
    sides = int(input("Enter the number of sides: "))
    side_length = float(input("Enter the side length (pixels): "))
    depth = int(input("Enter the recursion depth: "))

    # --- Turtle setup ---
    screen = turtle.Screen()    #Creates the drawing window.
    screen.title("Recursive Polygon Fractal")   #Sets the window title.

    t = turtle.Turtle() #Creates the turtle that draws.
    t.speed(0)          #Maximum speed (fastest).
    t.hideturtle()  #Hides the turtle icon; only shows lines.

    # Optional: center the polygon roughly
    t.penup()   #Lift the pen (move without drawing).
    t.goto(-side_length / 2.0, 0)   #Move to coordinates (-side_length/2, 0) so the drawing is more centered.
    t.pendown() #Put the pen down to start drawing.

    # Ensure the turtle faces to the right to start (Sets the turtle’s direction to 0 degrees)
    t.setheading(0) 

    # Draw the fractal polygon with inward indentation
    draw_fractal_polygon(t, sides, side_length, depth, inward=True)

    # Keep window open until click
    screen.exitonclick()

if __name__ == "__main__":  #Standard Python pattern. 
    main()  #Means: only run main() when this file is run directly, not when it’s imported as a module.