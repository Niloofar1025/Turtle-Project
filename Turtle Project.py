
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10358790
#    Student name: Niloofar Gorjinejad
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  LAND GRAB
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "process_moves".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various rectangular icons, using data stored in a
#  list to determine which icons to place and where.  See the
#  instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must NOT rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *

# Define constant values for setting up the drawing canvas
cell_width = 120 # pixels (default is 120)
cell_height = 90 # pixels (default is 90)
grid_size = 7 # width and height of the grid (default is 7)
x_margin = cell_width * 2.4 # pixels, the size of the margin left/right of the board
y_margin = cell_height // 2.1 # pixels, the size of the margin below/above the board
canvas_height = grid_size * cell_height + y_margin * 2
canvas_width = grid_size * cell_width + x_margin * 2

# Validity checks on grid size
assert cell_width >= 100, 'Cells must be at least 100 pixels wide'
assert cell_height >= 75, 'Cells must be at least 75 pixels high'
assert grid_size >= 5, 'Grid must be at least 5x5'
assert grid_size % 2 == 1, 'Grid size must be odd'
assert cell_width / cell_height >= 4 / 3, 'Cells must be much wider than high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You may NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(show_instructions = True, # show Part B instructions
                          label_locations = True, # label axes and home coord
                          bg_colour = 'light grey', # background colour
                          line_colour = 'grey'): # line colour for grid
    
    # Set up the drawing canvas with enough space for the grid
    setup(canvas_width, canvas_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible


    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coordinate of the grid
    left_edge = -(grid_size * cell_width) // 2 
    bottom_edge = -(grid_size * cell_height) // 2

    # Draw the horizontal grid lines
    setheading(0) # face east
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge, bottom_edge + line_no * cell_height)
        pendown()
        forward(grid_size * cell_width)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for line_no in range(0, grid_size + 1):
        penup()
        goto(left_edge + line_no * cell_width, bottom_edge)
        pendown()
        forward(grid_size * cell_height)

    # Optionally label the axes and centre point
    if label_locations:

        # Mark the centre of the board (coordinate [0, 0])
        penup()
        home()
        dot(30)
        pencolor(bg_colour)
        dot(20)
        pencolor(line_colour)
        dot(10)

        # Define the font and position for the axis labels
        small_font = ('Arial', (18 * cell_width) // 100, 'normal')
        y_offset = (32 * cell_height) // 100 # pixels

        # Draw each of the labels on the x axis
        penup()
        for x_label in range(0, grid_size):
            goto(left_edge + (x_label * cell_width) + (cell_width // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_size):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_height) + (cell_height // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

    # Optionally write the instructions
    if show_instructions:
        # Font for the instructions
        big_font = ('Arial', (24 * cell_width) // 100, 'normal')
        # Text to the right of the grid
        penup()
        goto((grid_size * cell_width) // 2 + 50, -cell_height // 3)
        write('This space\nreserved for\nPart B', align = 'left', font = big_font)
        
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    # Ensure any drawing still in progress is displayed
    update()
    
    # Optionally hide the cursor
    if hide_cursor:
        hideturtle()
    # Release the drawing canvas
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The data sets in this section are provided to help you develop and
# test your code.  You can use them as the argument to the
# "process_moves" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_moves" function appearing below.
# Your program must work correctly for any data set that can be
# generated by calling "random_moves()" with no argument.
#
# Each of the data sets is a list of moves, each specifying which
# competitor is attempting to move and in which direction.  The
# general form of each move is
#
#     [competitor_identity, direction]
#
# where the competitor identities range from 'Competitor A' to
# 'Competitor D' and the directions are 'Up', 'Down', 'Left' and
# 'Right'.
#
# Note that all the data sets below assume the second argument
# to "random_moves" has its default value.
#

# The following data set makes no moves at all and can be used
# when developing the code to draw the competitors in their
# starting positions.
fixed_data_set_00 = []

# The following data sets each move one of the competitors
# several times but do not attempt to go outside the margins
# of the grid or overwrite previous moves
fixed_data_set_01 = [['Competitor A', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor A', 'Up']]

fixed_data_set_02 = [['Competitor B', 'Left'],
                     ['Competitor B', 'Left'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor B', 'Right'],
                     ['Competitor B', 'Up']]

fixed_data_set_03 = [['Competitor C', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Right'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Down'],
                     ['Competitor C', 'Left']]
fixed_data_set_04 = [['Competitor D', 'Left'],
                     ['Competitor D', 'Left'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Right'],
                     ['Competitor D', 'Up'],
                     ['Competitor D', 'Right'],
                     ['Competitor D', 'Down']]

# The following data set moves all four competitors and
# will cause them all to go outside the grid unless such
# moves are prevented by your code
fixed_data_set_05 = [['Competitor C', 'Right'],
                     ['Competitor B', 'Up'],
                     ['Competitor D', 'Down'],
                     ['Competitor A', 'Left'],
                     ['Competitor C', 'Down'],
                     ['Competitor B', 'Down'],
                     ['Competitor D', 'Left'],
                     ['Competitor A', 'Up'],
                     ['Competitor C', 'Up'],
                     ['Competitor B', 'Right'],
                     ['Competitor D', 'Right'],
                     ['Competitor A', 'Down'],
                     ['Competitor C', 'Right'],
                     ['Competitor B', 'Down'],
                     ['Competitor D', 'Right'],
                     ['Competitor A', 'Right']]

# We can also control the random moves by providing a "seed"
# value N to the random number generator by using
# "random_moves(N)" as the argument to function "process_moves".
# You can copy the following function calls into the main
# program to force the program to produce a fixed sequence of
# moves while debugging your code.

# The following seeds all produce moves in which each
# competitor captures a small number of squares in their
# own corner, but do not interfere with one another.
#
#   random_moves(39) - Only one round occurs
#   random_moves(58) - Only two rounds
#   random_moves(12)
#   random_moves(27)
#   random_moves(38)
#   random_moves(41)

# The following seeds all produce moves in which two or
# more competitors overlap one another's territory.
#
#   random_moves(20) - Competitors C and D touch but don't overlap
#   random_moves(23) - Competitors A and B overlap
#   random_moves(15) - Competitors A and D overlap
#   random_moves(29) - Competitors B and D overlap slightly
#   random_moves(18) - Competitors B, C and D overlap
#   random_moves(31) - A and C overlap slightly, B and D touch but don't overlap
#   random_moves(36) - Competitor D overlaps Competitor C
#
# We haven't yet found a seed that causes a player to
# be completely eliminated - can you find one?

# The following seeds all produce very long sequences of
# moves which result in most of the grid being filled.
#
#   random_moves(19)
#   random_moves(75)
#   random_moves(43) - Competitor D reaches opposite corner
#   random_moves(87) - C occupies A's corner and A occupies B's corner
#   random_moves(90) - Only 4 squares left unoccupied
#
# We haven't yet found a seed that causes every cell
# to be occupied - can you find one?

# The following seeds produce data sets which have a special
# meaning in the second part of the assignment. Their
# significance will be explained in the Part B instructions.
#
#   random_moves(21)
#   random_moves(26)
#   random_moves(24)
#   random_moves(35)
#
#   random_moves(52)
#   random_moves(51)
#   random_moves(47)
#   random_moves(46)
#
#   random_moves(53)
#   random_moves(62)
#   random_moves(81)
#   random_moves(48)
#
#   random_moves(54)
#   random_moves(98)

# If you want to create your own test data sets put them here.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.

# The following function creates a random data set as a list
# of moves.  Your program must work for any data set that
# can be returned by this function.  The results returned by
# calling "random_moves()" will be used as the argument to your
# "process_moves" function during marking.  For convenience during
# code development and marking this function also prints each move
# to the shell window.
#
# NB: As a matter of style your code should not print anything else
# to the shell.  Make sure any debugging calls to the "print"
# function are disabled before you submit your solution.
#
# The function makes no attempt to avoid moves that will go
# outside the grid.  It is your responsibility to detect and
# ignore such moves.
#
def random_moves(the_seed = None, max_rounds = 35):
    # Welcoming message
    print('\nWelcome to Land Grab!')
    print('Here are the randomly-generated moves:')
    # Set up the random number generator
    seed(the_seed)
    # Randomise the order in which competitors move
    competitors = ['Competitor A', 'Competitor B', 'Competitor C', 'Competitor D',]
    shuffle(competitors)
    # Decide how many rounds of moves to make
    num_rounds = randint(0, max_rounds)
    # For each round generate a random move for each competitor
    # and save and print it
    moves = []
    for round_no in range(num_rounds):
        print()
        for competitor in competitors:
            # Create a random move
            move = [competitor, choice(['Left', 'Right', 'Up', 'Down'])]
            # Print it to the shell and remember it
            print(move)
            moves.append(move)
    # Print a final message and return the list of moves
    print('\nThere were', len(competitors) * num_rounds,
          'moves generated in', num_rounds,
          ('round' if num_rounds == 1 else 'rounds'))
    return moves

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "process_moves" function.
#

 #Draw competitors on the grid as per the provided data set

tracer (False)

penup()
goto(-550,280)
write("competitor A: Bird", font = ('Arial', 16))
 
counter = 0
def draw_bird(x,y):
    # background color of bird

    penup() #start drawing
    goto(x,y)  # goto absolute coordinates (-420,255) ---- (x,y)
    fillcolor("light yellow")
    begin_fill()  #fill the shape drawn between these two statements
    for background in range (2):  # do the two same drawings actions 2 times
        fd(120) #move forward 120 pixels
        right(-90) # turn right by -90 degrees
        fd(90)  # move forward 90 pixels
        right(-90)  # turn right by -90 degrees
    end_fill()  # fill the shape drawn between these two statements with the light yellow colour

    # draw the body of bird

    radius = 25 # giving a same values for the radius
    penup() # Turtle will move around the screen, but will not draw when its pen state is PENUP
    goto(x+20,y+ 5)  # goto absolute coordinates (-400,240)
    left(45) # turn left by 45 degrees
    fd(radius)  # move forawrad 25 pixels , as radius equals 25
    pendown() # start drawing 
    right(90) # turn right by 90 degree
    color("orange") # color control
    fillcolor("orange")  # fill the shape drawn between these two statements with the light yellow colour
    begin_fill() 
    circle(radius) #set the default colour to 25 , as radius= 25
    end_fill()  #fill the shape drawn between these two statements with the current colour

    # draw the big eyes of bird

    radius = 15   # giving a same values for the radius
    penup()   # Turtle will move around the screen, but will not draw when its pen state is PENUP
    goto(x + 55,y + 45) #goto absolute coordinates (-365,280) which moves the eyes of bird
    left(45) # turn left by 45 degree
    fd(radius / 2) # move forward by (radius/2) , as we defined the radius by 15 degrees, it will be easier to devide it by 2 if it's big
    pendown() # start drawing 
    right(90) # turn right by 90 degree
    color("yellow")
    fillcolor("yellow")
    begin_fill()
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()

    #draw the medium eyes of bird

    radius = 10
    penup() # not drawing while it's moving
    goto(x + 65,y + 52) #goto absolute coordinates (-359,285) which is the coordinates of medium eye of bird 
    left(45) # turn left by 45 degree 
    fd(radius / 2) # move forward by given radius 
    pendown() # pull the pen down, drawing when it's moving
    right(90) # turn right by 90 degree
    color("black")
    fillcolor("black") # fill the shapes with black colour
    begin_fill()
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()

    # draw the detail of eye
    
    radius = 5  # giving a same values for the radius
    penup()  # not drawing while it's moving
    goto(x+75,y+50) # (-420+55, 255+20)
    left(45)
    fd(radius / 2)
    pendown()  # start drawing 
    right(90) # turn right by 90 degree
    color("white") # draw a circle with given radius 
    fillcolor("white")
    begin_fill()  #fill the shape drawn between these two statements
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()

    # draw the first dots of bird

    radius = 5  # giving a same values for the radius
    penup()  # not drawing while it's moving
    goto(x+50,y+40) 
    pendown()  # start drawing 
    color("white")
    fillcolor("white")
    begin_fill()  #fill the shape drawn between these two statements
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()

    # draw the second dots of bird

    radius = 5  # giving a same values for the radius
    penup()  # not drawing while it's moving
    goto(x+40,y+55) #goto(-375,270)
    pendown()  # start drawing 
    color("white")
    fillcolor("white")
    begin_fill() 
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()


    # draw the third dot??s of bird

    radius = 5   # giving a same values for the radius
    penup()  # not drawing while it's moving
    goto(x+35,y+40)#goto(-370,280)
    pendown()  # start drawing 
    color("white")
    fillcolor("white")
    begin_fill()  #fill the shape drawn between these two statements
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()


    # draw the fifth dots of bird

    radius = 5  # giving a same values for the radius
    penup()  # not drawing while it's moving
    goto(x+45,y+25) #(370,280)
    pendown()  # start drawing 
    color("white")
    fillcolor("white")
    begin_fill()  #fill the shape drawn between these two statements
    circle(radius / 2) # draw a circle with given radius 
    end_fill()

    # draw the sixth dots of bird

    radius = 5  # giving a same values for the radius
    penup()
    goto(x+60,y + 30) #goto(-360,290)
    pendown()  # start drawing 
    color("white")
    fillcolor("white")
    begin_fill()   #fill the shape drawn between these two statements
    circle(radius / 2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()

    # draw the neb of bird

    radius = 5   # giving a same values for the radius
    penup()  # not drawing while it's moving
    goto(x+82,y + 38) #(-345,275)
    pendown()  # start drawing 
    right(90) # turn right by 90 degree
    color("red")
    fillcolor("red")
    begin_fill()  #fill the shape drawn between these two statements
    circle(radius / 2)  # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()
    setheading(0) # set the orientation of the turtle to 0 degree
    penup()   # not drawing while it's moving
  



penup()
goto(450, 280)
write("competitor B: Koala", font = ('Arial', 16))


# Draw Koala

def draw_Koala(x,y):

    #print(x,y)
    penup()
    goto(x,y)  #goto (300,-315)
    fillcolor("white")
    begin_fill()  #fill the shape drawn between these two statements with the light yellow colour
    # do the two same drawings actions 2 times
    for background in range (2):
        fd(120) #move forward 120 pixels
        right(-90) # turn right by -90 degrees
        fd(90)  # move forward 90 pixels
        right(-90)  # turn right by -90 degrees
    end_fill()  # fill the shape drawn between these two statements with the light yellow colour

 

    # draw the body of Koala
    radius = 20 # giving a same values for the radius
    goto(x + 60, y + 20)
    color("grey")
    fillcolor("grey")
    begin_fill()  #fill the shape drawn between these two statements with the light yellow colour
    circle(radius)
    end_fill() #fill the shape drawn after the call begin_fill()

    # Koala left ear
    penup()  # not drawing while it's moving
    goto(x + 45 ,y + 48)
    pendown() # drawing when it's moving
    color("light grey")
    fillcolor("light grey")
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2)
    end_fill() #fill the shape drawn after the call begin_fill()
    
    # Koala left ear
    penup()   # not drawing while it's moving
    goto(x + 80 ,y + 45)
    pendown() # start drawing
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2)
    end_fill() #fill the shape drawn after the call begin_fill()
    

    # Koala right nose
    penup()   # not drawing while it's moving
    goto(x + 60 ,y + 30)
    pendown() # drawing when it's moving
    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/ 6)
    end_fill() #fill the shape drawn after the call begin_fill()
  

    # Koala right nose
    penup()   # not drawing while it's moving
    goto(x + 70 ,y + 40)
    pendown() # start drawing 
    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/ 12)
    end_fill() #fill the shape drawn after the call begin_fill()


    # Koala left eye
    penup()   # not drawing while it's moving
    goto(x + 50 ,y + 40)
    pendown() # start drawing
    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/ 12)
    end_fill() #fill the shape drawn after the call begin_fill()
    penup()



penup()
goto(-570, -280)
write("competitor C: Fox", font = ('Arial', 16))

def draw_fox(x,y):

    # draw the background color of fox
    speed(5)
    penup() # not drawing when moving 
    goto(x,y) # goto absolute coordinates 
    setheading(-90)
    fillcolor("light blue")
    begin_fill() #fill the shape drawn between these two statements
    for background in range (2):
        fd(-90) # move forawrd by -90 pixels 
        right(-90) # turn right by -90 degree
        fd(120) # move forawrd by 120 pixels 
        right(-90) # turn right by -90 degree
    end_fill() #fill the shape drawn after the call begin_fill()


    # draw the head of Fox

    penup()
    color("brown")
    fillcolor("brown")
    begin_fill() #fill the shape drawn between these two statements
    goto( x + 100,y + 75)  # (-420,-315) ---- (-320,-240)
    left(-90) # turn left by -90 degree
    forward(80) # move forawrd by 80 pixels 

    for action in range(2):
        left(120) # turn left by 120 degree
        forward(80) # move forward by 80 pixels 
    end_fill() #fill the shape drawn after the call begin_fill()

     #draw the right eye of Fox with star

    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    goto( x + 70, y + 55) # (-420,-315) ---- (-350,-260)

    for action in range (5):
        fd(25)  # move forward by 25 pixels 
        right(144)  # turn right by 144 degree

    end_fill() #fill the shape drawn after the call begin_fill()
  

    # draw the right eye of Fox with star
    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    goto(x + 30 , y + 55) # (-420,-315) ---- (-390,-260)

    for action in range (5):# do the same two drawing actions 5 times
        fd(25) # move forward by 25 pixels
        right(144) # turn right by 144 

    end_fill() #fill the shape drawn after the call begin_fill()
    ht()

    # draw the nose of Fox with circle function

    radius= 10
    penup() # moving but not drawing 
    goto( x + 63, y + 25) # (-420,-315) ---- (-357,-290)
    left(45)
    fd(radius/2)
    pendown() # drawing when it's moving
    right(90)
    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2)
    end_fill() #fill the shape drawn after the call begin_fill()

    # draw the right ear of Fox with triangle

    penup() # moving but not drawing 
    color("black")
    fillcolor("black")
    begin_fill() #fill the shape drawn between these two statements
    goto( x + 90,y + 75) # (-420,-315) ---- (-330,-240)
    setheading(210)
    left(-90)
    forward(15)
    for action in range(2):
        left(120)
        forward(15)
    end_fill()  #fill the shape drawn after the call begin_fill()    
            

    # draw the right ear of Fox with triangle

    penup() # moving but not drawing 
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    goto( x + 50,y + 75) # (-420,-315) ---- (-370,-240)
    setheading(210)
    left(-90) #  turn left by -90 degree
    forward(15) # move forward by 15 pixles 
    for action in range(2): # do the same two drawing actions 2 times 
        left(120) # turn left by 120 degree
        forward(15) # move forward by 15 pixles 
    end_fill() #fill the shape drawn after the call begin_fill()
    setheading(0)
    penup() # not drawing while it's moving 


penup() # moving but not drawing 
goto(450, -280) # goto the absolute coordinate
write("competitor D: Ladybug", font = ('Arial', 16))

def draw_ladybug(x,y):


    # background color of Ladybug

    penup() # not drawing when moving
    goto(x,y)  #goto(300, -315)---- # (300,-225)
    setheading(-270)
    fillcolor("light green")
    begin_fill() #fill the shape drawn between these two statements
    for background in range (2):
        fd(90) # move forward
        right(90) # turn right by 90 degree
        fd(120) #move forward
        right(90) # turn right by 90 degree
    end_fill()  #fill the shape drawn after the call begin_fill()

    # draw the head of ladybug

    radius= 20
    penup() # not drawing when moving 
    goto(x + 65,y + 25) # (300,-315)--------#(350, -245)
    left(45) # turn left by 45 degrees 
    fd(radius/2) # move forward 
    pendown() # start drawing 
    right(90) # turn right by 90 degree
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()


    # draw the body of ladybug
    radius= 40
    penup() # not drawing when moving 
    goto(x + 85, y + 40 ) # (300,-315)-------- # goto(350,-240) 
    color("red") # set the pencolour and fill the colour 
    fillcolor("red")
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill()  #fill the shape drawn after the call begin_fill()

    
    # draw the first eyes of ladybug

    radius= 5
    penup() # not drawing when it's moving 
    goto(x + 40 ,y + 34 )# goto(300,-225) --------#(375,-250)
    pendown() # drawing when it's moving
    color("white") # set the pencolour and fill the colour 
    fillcolor("white") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()



    # draw the second eyes of ladybug

    radius= 5
    penup()  # not drawing when it's moving 
    goto(x + 45 ,y + 25) # goto(300,-225) ------#(370,-250)
    left(45) # turn left by 45 degree
    fd(radius/2) # move forward 
    pendown() # drawing when it's moving
    right(90) # turn right by 90 degree
    color("white") # set the pencolour and fill the colour 
    fillcolor("white") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill()  #fill the shape drawn after the call begin_fill()


    # draw the first dot of ladybug

    radius= 5
    penup() # not drawing when moving 
    goto(x + 60,y + 55) # goto(300,-225) --------#(360,-280)
    pendown() # drawing when it's moving
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()


    # draw the second dot of ladyug

    radius= 5
    penup() # not drawing when moving 
    goto(x + 72, y + 65) # goto(300,-225) --------#(350,-270))
    pendown() # start drawing 
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill()  #fill the shape drawn after the call begin_fill() 


    # draw the third dot of ladybug

    radius= 5
    penup() # not drawing when moving 
    goto(x + 82 ,y + 60) # goto(300,-225) --------#(340,-290)
    pendown()  # start drawing 
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill() #fill the shape drawn after the call begin_fill()

    # draw the forth dot of ladybug

    radius= 5
    penup() # not drawing when moving 
    goto(x + 80 ,y + 50)  # goto(300,-225) --------#(330,-278)
    pendown()  # start drawing 
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour 
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill()  #fill the shape drawn after the call begin_fill()

    # draw the fifth dot of ladybug

    radius= 5
    penup() # not drawing when moving 
    goto(x + 75,y + 45)  #goto(300,-225) --------#(350,-290)
    pendown()  # start drawing 
    color("black") # set the pencolour and fill the colour 
    fillcolor("black") # set the fill colour
    begin_fill() #fill the shape drawn between these two statements
    circle(radius/2) # draw a circle with given radius 
    end_fill()  #fill the shape drawn after the call begin_fill() 
    setheading(0) # set the orientation of the turtle to 0 angle
    penup() # moving but not drawing 


def competitor (positions): # define the movement of each competitor 
    if positions == "competitor A":
        return positions [0][0], positions[0][1]
    if positions == "competitor B":
        return positions [1][0], positions [1][1]
    if positions == "competitor C":
        return positions [2][0], positions[2][1]
    if positions == "competitor D":
        return positions [3][0],positions [3][1]

def changing_positions(positions):  
    if positions == "competitor A":
        positions [0] == position()
    if postions == "compeittor B":
        positions[1] == position()
    if postions == "compeittor C":
        positions[2] == position()
    if postions == "compeittor D":
        positions[3] == position()

def movement_process(move): 

    #Move
    if move == "Right" and round(xcor()) < 300: # turn right 
        setheading(0) # set the orientation of the turtle to 0 degree
        fd(120) # move forawrd by 120 pixels 

    elif move == "Left" and round(xcor()) > -420: # turn left
        setheading(180) # set the orientation of the turtle to 180 degree
        fd(120)  # move forawrd by 120 pixels 
    elif move == "Up" and round(ycor()) < 225: # turn up 
        setheading(90) # set the orientation of the turtle to 90 degree
        fd(90)  # move forawrd by 90 pixels 
    elif move == "Down" and round(ycor()) > -315: # turn down 
        setheading(270) # set the orientation of the turtle to 270 degree
        fd(90)  # move forawrd by 90 pixels 
        
    setheading(0) # set the orientation of the turtle to 0 angle

    
    x= xcor()
    y = ycor()

    x = round (x)
    y = round (y)
   


    return [x, y]
    
     

def process_moves(moves): # define what process should do
    global counter
    positions = [[-420,225], [300,225],[-420,-315], [300,-315]] # creating list for each corner
    draw_bird(positions[0][0],positions[0][1]) #[-420,225] ---- index of -420 is [0][0], index of 225 is [0][1]
    draw_Koala(positions[1][0],positions[1][1]) #[300,225] ---- index of 300 is [1][0], index of 225 is [1][1]
    draw_fox(positions[2][0],positions[2][1]) #[-420,-315] ---- index of -420 is [2][0], index of -315 is [2][1]
    draw_ladybug(positions[3][0],positions[3][1]) #[300,-315] ---- index of 300 is [3][0], index of -315 is [3][1]


    for move in moves:
        
        if move[0] == "Competitor A":
            goto(positions[0]) #Goto position of competitor A
            positions[0] = movement_process(move[1]) 
            draw_bird(positions[0][0], positions[0][1]) # draw bird by identifying it in process moves


        
            if positions[0] == [-60, -45] and counter == 0: # position A, go find the centre, use counter to update the position each time
                penup() # not drawing while it's mop
                goto(460,-40) #find out where to print on part B
                draw_bird(460,-40) # draw the competitor 
                goto(-60,-45)   # go back to where you were (-60,-45) 
                counter = counter + 1   # add 1 to counter to update the positions 
                


        elif move[0] == "Competitor B":
            goto(positions[1]) #Goto position of competitor B
            positions[1] = movement_process(move[1])
            draw_Koala(positions[1][0], positions[1][1]) # draw Koala by identifying it in process moves
           
            

            if positions[1] == [-60, -45] and counter ==0:  # comeptitor B, starts in a centre and update a position by "counter"
                penup()  # not drawing while it's moving
                goto(460,-50) # goto part B area
                draw_Koala(460,-40) # draw Koala in part B positions 
                goto(-60,-45) # go back to where you were (-60,-45) 
                counter = counter + 1  # add 1 to counter to update the positions 


        elif move[0] == "Competitor C":
            goto(positions[2]) #Goto position of competitor C
            positions[2] = movement_process(move[1])
            draw_fox(positions[2][0], positions[2][1]) #draw fox by identifying it in process moves

            if positions[2] == [-60, -45] and counter ==0: # comeptitor C, starts in a centre and update a position by "counter"
                penup()  # not drawing while it's moving
                goto(460,-40) # goto part B area
                draw_fox(460,-40) # draw fox in part B position 
                goto(-60,-45)   # go back to where you were (-60,-45) 
                counter = counter + 1  # add 1 to counter to update the positions 
                       

        elif move[0] == "Competitor D": 
            goto(positions[3]) #Goto position of competitor D
            positions[3] = movement_process(move[1]) 
            draw_ladybug(positions[3][0], positions[3][1]) # draw ladybug  by identifying it in process moves

    

            if positions[3] == [-60, -45] and counter ==0: # comeptitor D, starts in a centre and update a position by "counter"
                
                penup()  # not drawing while it's moving
                goto(440,-40) #goto part B area
                draw_ladybug(460,-40) # draw ladybug in part B positions 
                goto(-60,-45) # go back to where you were (-60,-45) 
                counter = counter + 1  # add 1 to counter to update the positions
                
        
    if counter == 0: 
        goto(460,-40)
        write("No competitor reached the house" , font = ('Arial', 16))

    elif counter > 0:   
          goto(440,-60)
          write("First competitor reaches the house" , font = ('Arial', 14))
            

    
        

   
    

    
        



#--------------------------------------------------------------------#


#-----Main Program---------------------------------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution, and calls your solution.  Do not change
# any of this code except as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, choose
# ***** whether or not to label the axes, etc, by providing
# ***** arguments to this function call
               
create_drawing_canvas(show_instructions=False)


# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('slowest')

# Decide whether or not to show the drawing step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** theme and its competitors
title('Animals, Koala, Bird, Ladybug and Fox')

### Call the student's function to process the moves
### ***** While developing your program you can call the
### ***** "random_moves" function with a fixed seed for the random
### ***** number generator, but your final solution must work with
### ***** "random_moves()" as the argument to "process_moves", i.e.,
### ***** for any data set that can be returned by calling
### ***** "random_moves" with no seed.

#process_moves(random_moves()) # <-- this will be used for assessment

### Alternative function call to help debug your code
### ***** The following function call can be used instead of
### ***** the one above while debugging your code, but will
### ***** not be used for assessment. Comment out the call
### ***** above and uncomment the one below if you want to
### ***** call your "process_moves" function with one of the
### ***** "fixed" data sets above, so that you know in advance
### ***** what the moves are.


#process_moves(fixed_data_set_04) # <-- not used for assessment


process_moves(random_moves())


# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid.
release_drawing_canvas()

#
#--------------------------------------------------------------------#
