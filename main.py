import turtle as t
import random
t.colormode(255)
timmy = t.Turtle()
timmy.hideturtle()




color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), 
(82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]

xcor = -212.13
ycor = -212.13
timmy.penup()
timmy.speed("fastest")
timmy.goto(xcor, ycor)
for i in range(100):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    print(timmy.position())
    if timmy.position() == (287.87, ycor):
        new_ycor = 50
        ycor += new_ycor
        timmy.goto(xcor, ycor)


















screen = t.Screen()
screen.screensize(10, 10)
screen.mainloop()












