from turtle import *

def main():
    speed(10)
    bgcolor('lightblue')
    penup()

    goto(0, -200)
    pendown()
    pensize(5)
    pencolor('yellow')
    circle(200)
    penup()

    goto(-80, 50)
    pendown()
    pencolor('blue')
    begin_fill()
    circle(40)
    end_fill()
    penup()

    goto(80, 50)
    pendown()
    pencolor('blue')
    begin_fill()
    circle(40)
    end_fill()
    penup()

    goto(-80, 50)
    pendown()
    pencolor('green')
    begin_fill()
    circle(25)
    end_fill()
    penup()

    goto(80, 50)
    pendown()
    pencolor('green')
    begin_fill()
    circle(25)
    end_fill()
    penup()

    goto(0, -100)
    pendown()
    pencolor('red')
    begin_fill()
    circle(20)
    end_fill()
    penup()

main()
