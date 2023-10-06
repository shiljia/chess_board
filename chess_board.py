
import turtle

t=turtle.Turtle()

t._tracer(3)
t.pu()
t.goto(-390,-390)
t.pd()

c=0

for k in range(8):
    for j in range(8):
        if(c%2==0):
            clr='black'
        else:
            clr='white'

        t.fillcolor(clr)
        t.begin_fill()

        for i in range(4):
            t.fd(100)
            t.lt(90)
        t.end_fill()
        c+=1
        t.fd(100)
    c+=1
    t.pu()
    t.goto(t.pos()[0]-800,t.pos()[1]+100)
    t.pd()
            
