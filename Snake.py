import turtle as turtle
import random
import math
WINDOW_SIZE = 600
SEGMENTS = 0
MAX_SEGMENTS = 500
LENGTH = 1
MAX_LENGTH = 20
THICKNESS = 1
MAX_THICKNESS = 10
ANGLE = -30
MAX_ANGLE = 30
HEADING_DIRECTION = 0
RANDOM_LENGTH = random.randint(LENGTH, MAX_LENGTH)
RANDOM_THICKNESS = random.randint(THICKNESS, MAX_THICKNESS)
RANDOM_DIRECTION = random.randint(0, 360)
RANDOM_ANGLE = random.randint(ANGLE, MAX_ANGLE)

def init():
    turtle.setworldcoordinates(-500, -500, 500, 500)
    turtle.speed(100)

def boundingbox():
    turtle.penup()
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(400)
    turtle.right(90)
    turtle.forward(200)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

def drawSnakeRec(SEGMENTS,length):
    total_length = 0
    if SEGMENTS == 0:
        pass
    else:
        turtle.forward(LENGTH)
        total_length += length
        turtle.left(MAX_ANGLE)
        total_length += drawSnakeRec(SEGMENTS-1, length-1)
    return total_length


def drawSnakeRec(SEGMENTS,LENGTH):
    total_length = 0
    if SEGMENTS == 0:
        pass
    else:
        turtle.pencolor(random.random(), random.random(), random.random())
        turtle.pensize(RANDOM_THICKNESS)
        turtle.forward(RANDOM_LENGTH)
        turtle.left(RANDOM_ANGLE)
    tx, ty = turtle.position ()
    if (tx > 200) or (ty < -200) or (ty > 200) or (ty < -200):
        turtle.forward(RANDOM_LENGTH)
    else:
        turtle.right(180)
        turtle.forward(RANDOM_LENGTH)
        total_length += drawSnakeRec(SEGMENTS - 1, MAX_LENGTH)
    return total_length

    if (random_direction > 180) and (random_direction < 0):
            if x - random_length < -200:
                random_direction += 180 % 0
                print("71: " + str(x) + " " + str(y))
                # Random direction is the angle that is used.
        if (random_direction < 180) and (random_direction > 0):
            if x + random_length > 200:
                random_direction += 180 % 0
                print("76: " + str(x) + " " + str(y))
        if (random_direction > 90) and (random_direction < 270):
            if y - random_length < -200:
                random_direction += 180 % 0
                print("80: " + str(x) + " " + str(y))
        if (random_direction < 270) or (random_direction > 90):
            if y + random_length > 200:
                random_direction += 180 % 0
                print("84: " + str(x) + " " + str(y))
            turtle.setheading(random_direction)
            turtle.right(random_angle)
            turtle.forward(random_length)
            total_length += randomSnakeRec(SEGMENTS - 1, MAX_LENGTH)
        return total_length


        txt = math.cos(random_angle)*random_length
        tyt = math.sin(random_angle)*random_length

        #turtle.setheading(random_angle)
        if random_angle >= 0:
            turtle.right(random_angle)
        else:
            turtle.left(abs(random_angle))
        if(txt + tx > -190) and (txt + tx < 190) and (tyt + ty > -190) and (tyt + ty < 190):
            turtle.forward(random_length)
            print("forward: " + str(random_length) + " segments: " + str(SEGMENTS))
        else:
            turtle.right(180)
            turtle.forward(random_length)
        total_length += randomSnakeRec(SEGMENTS - 1, MAX_LENGTH)
    return total_length

def main():
    MAX_SEGMENTS = int(input("Segments (0-500): "))
    while True:
        if MAX_SEGMENTS <= 0 or MAX_SEGMENTS <= 500:
            break
        MAX_SEGMENTS = int(input("Segments is out of range. Segment must be between 0 and 500 inclusive. Try again. Segments (0-500): "))
    init()
    turtle.hideturtle()
    boundingbox()
    drawSnakeRec(MAX_SEGMENTS, MAX_LENGTH)
    print("The snake's length is",total_length,"unit.")
    input("Push enter to continue")
    turtle.clear()
    turtle.setup(window_size, window_size)
    turtle.speed(0)
    turtle.setpos(0,0)
    boundingbox2()
    drawSnakeIter(4, 10)
    randomSnakeIter(MAX_SEGMENTS)
    print("The snake's length is",randomSnakeRec,"unit.")
    turtle.bye()
    turtle.mainloop()

if __name__ == "__main__":

    main()
