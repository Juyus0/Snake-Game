from turtle import Turtle, Screen #It's like Math in java
import time
import random

def up(): #method in java 
    if snakes[0].heading() != 270: #when not down down ,, heading is the method in turtle library
        snakes[0].setheading(90)

def down():
    if snakes[0].heading() != 90:
        snakes[0].setheading(270)

def right():
    if snakes[0].heading() != 180:
        snakes[0].setheading(0)

def left():
    if snakes[0].heading() != 0:
        snakes[0].setheading(180)

def create_snake(pos):
    snake_body = Turtle()
    snake_body.shape("square")
    snake_body.color("orangered")
    snake_body.up()
    snake_body.goto(pos)
    snakes.append(snake_body) #appending!

def rand_pos():
    rand_x = random.randint(-250, 250)
    rand_y = random.randint(-250, 250)
    return rand_x, rand_y

def score_update():
    global score
    score += 1
    score_pen.clear()
    score_pen.write(f"Score: {score}", font = ("", 15, "bold"))

def game_over(reason=""): #why died
    score_pen.goto(0, 0)
    if reason:
        score_pen.write(f"Game Over: {reason}", False, "center", ("", 30, "bold"))
    else:
        score_pen.write("Game Over", False, "center", ("", 30, "bold"))

def change_snake_color(color):
    for segment in snakes:
        segment.color(color)


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Khaki")
screen.title("Snake Game")

# snake
start_pos = [(0, 0), (-20, 0), (-40, 0)]
snakes = []
score = 0
for pos in start_pos: 
    create_snake(pos)

# food
food = Turtle()
food.shape("circle")
food.color("snow")
food.up()
food.speed(0)
food.goto(rand_pos())

# score
score_pen = Turtle()
score_pen.ht()
score_pen.up()
score_pen.goto(-270, 250)
score_pen.write(f"Score: {score}", font=("", 15, "bold"))

screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")




game_on = True
while game_on:
    screen.update()
    time.sleep(0.1) #for smoothing the animation of the snake

    for i in range(len(snakes) - 1, 0, -1): # updating the position of each parts of the snake's body
        snakes[i].goto(snakes[i - 1].pos())

    snakes[0].forward(20)

    # Random chance of heart attack
    if random.randint(1, 200) == 1:
        change_snake_color("gray")
        game_on = False
        game_over("Heart Attack")
        break

    if snakes[0].distance(food) < 15:
        # Random chance of food poisoning
        if random.randint(1, 100) == 1:
            change_snake_color("green")
            game_on = False
            game_over("Food Poisoning")
            break
        score_update()
        food.goto(rand_pos())
        # Grow the snake from the tail
        tail = snakes[-1].pos()
        create_snake(tail)

    if snakes[0].xcor() > 280 or snakes[0].xcor() < -280 or snakes[0].ycor() > 280 or snakes[0].ycor() < -280: #collisions
        game_on = False
        game_over()
        break

    for body in snakes[1:]:
        if snakes[0].distance(body) < 10:
            game_on = False
            game_over()
            break

screen.mainloop()
