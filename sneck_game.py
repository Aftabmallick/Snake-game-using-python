import turtle
import time
import random
import winsound
delay = 0.1
score = 0
high_score = 0
#window screen
wn= turtle.Screen()
wn.title("sneck By @Aforaftab")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)
#Sneck head
head= turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.shapesize(stretch_wid=.75,stretch_len=.75)
head.penup()
head.goto(0,0)
head.direction = "Stop"

#Sneak food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("blue")
food.penup()
food.goto(0,100)
#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0",align="center",font=("Courier",20,"normal"))
#up function
def goup():
    if head.direction !="down":
        head.direction ="up"
    
def godown():
    if head.direction !="up":
        head.direction ="down"
    
def goright():
    if head.direction !="left":
        head.direction ="right"
    
def goleft():
    if head.direction !="right":
        head.direction ="left"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
segments= []
wn.listen()
wn.onkeypress(goleft,"a" or "Left")
wn.onkeypress(goright,"d" or "Right")
wn.onkeypress(goup,"w" or "Up")
wn.onkeypress(godown,"s" or "Down")

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290 :
        
        winsound.PlaySound('gameover.wav',winsound.SND_FILENAME)
        head.goto(0,0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    if head.distance(food)<20:

        food.goto(random.randint(-270,270),random.randint(-270,270))
        #tail add
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("yellow")  
        new_segment.penup()
        segments.append(new_segment)
        winsound.PlaySound('eat.wav',winsound.SND_FILENAME | winsound.SND_ASYNC)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segment.clear()
            
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("Courier", 20, "normal"))
    time.sleep(delay)
