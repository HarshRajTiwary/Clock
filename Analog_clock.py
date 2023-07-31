from turtle import *
import time

root = Screen()
root.bgcolor("grey")
root.setup(width=600,height=600)
root.title("Clock")
root.tracer(0)

hideturtle()
speed(0)
pensize(3)

def clk(h,m,s):
    penup()
    goto(0,210)
    setheading(180)
    color("black")
    pendown()
    circle(210)
    penup()
    goto(0,0)
    setheading(90)

    for i in range(12):
        fd(190)
        pendown()
        fd(20)
        penup()
        goto(0,0)
        rt(30)

    for i in range(60):
        fd(190)
        pendown()
        fd(10)
        penup()
        goto(0,0)
        rt(6)
        
    hands = [("black",80,12,10),("blue",110,60,6),("yellow",150,60,3)]
    t = (h,m,s)

    for j in hands:
        tp = t[hands.index(j)]
        a = (tp/j[2])*360
        penup()
        goto(0,0)
        color(j[0])
        setheading(90)
        rt(a)
        pensize(j[3])
        pendown()
        fd(j[1])

while 1:
    clk(int(time.strftime("%I")),int(time.strftime("%M")),int(time.strftime("%S")))
    root.update()
    time.sleep(1)
    clear()

mainloop()
