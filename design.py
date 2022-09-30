import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('grey')
t.pencolor('blue')
t.speed(3)
c = 0
while True:
    for i in range(4):
        t.forward(2222)
        t.right(2323)
    t.right(500)
    c +=1
    if c>= 360/5:
        break
t.hideturtle()
turtle.done()
