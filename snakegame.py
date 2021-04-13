from random import randint
import turtle as t


t.bgcolor('yellow')

caterpiller = t.Turtle()   # caterpiller sprite
caterpiller.shape('square')
caterpiller.color('red')
caterpiller.speed(0)
caterpiller.penup()
caterpiller.hideturtle()

leaf = t.Turtle()  # food/leaf/goal
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14))  # draws a leaf/food
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

game_started = False
text_turtle = t.Turtle()
text_turtle.write\
                   (' Snake eats leafs \nPress SPACE to start\nDavid Ikin(c) 2021  '\
                    , align='center', font=('Arial', 18, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()  # SCORE
score_turtle.hideturtle()
score_turtle.speed(0)  # this turtle needs to stay put, so it can update player score


def outside_window():
    left_wall = -t.window_width() / 2
    right_wall = t.window_width() / 2
    top_wall = t.window_height() / 2
    bottom_wall = -t.window_height() / 2
    (x, y) = caterpiller.pos()
    outside = \
            x< left_wall or \
            x> right_wall or \
            y< bottom_wall or \
            y> top_wall
    return outside


def game_over():
    caterpiller.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('Game Over', align='center', font=('Arial', 30, 'normal'))


def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width() / 2) - 50
    y = (t.window_height() / 2) - 50  # 50 pixels from the right
    score_turtle.setpos(x, y)
    score_turtle.write(str(current_score), align='right', font=('Arial', 40, 'bold'))
    

def place_leaf():
    leaf.ht()
    leaf.setx(randint(-200, 200))
    leaf.sety(randint(-200, 200))
    leaf.st()


def start_game():
    global game_started
    if game_started:
        return
    game_started = True

    score = 0 
    text_turtle.clear()

    caterpiller_speed = 2
    caterpiller_length = 3
    caterpiller.shapesize(1, caterpiller_length, 1)
    caterpiller.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpiller.forward(caterpiller_speed)
        if caterpiller.distance(leaf) < 20:
            place_leaf()  #the current leaf has been eaten, so this bit of code adds a new one to the canvas
            caterpiller_length = caterpiller_length + 1  # caterpiller growth and potential difficulty setting feature
            caterpiller.shapesize(1, caterpiller_length, 1)  #growth
            caterpiller_speed = caterpiller_speed + 1
            score = score + 10
            display_score(score)
        if outside_window():
            game_over()
            break


def move_up():  #problem????
    if caterpiller.heading() == 0 or caterpiller.heading() == 180:  # checks if its heading left or right
        caterpiller.setheading(90)
        


def move_down():
    if caterpiller.heading() == 0 or caterpiller.heading() == 180:
        caterpiller.setheading(270)
        t.listen()


def move_left():
    if caterpiller.heading() == 90 or caterpiller.heading() == 270:
        caterpiller.setheading(180)
        t.listen()


def move_right():
    if caterpiller.heading() == 90 or caterpiller.heading() == 270:
        caterpiller.setheading(0)
        t.listen()

t.onkey(start_game, 'space')  #listen for the keyboard input, in this case space bar starts the game - onkey links direction function to the keyboard below

t.onkey(move_up, 'Up')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.onkey(move_right, 'Right')

t.listen()  #allows game to recieve a signal from input device, which is the keyboard

while True:
    t.mainloop()

        


        
