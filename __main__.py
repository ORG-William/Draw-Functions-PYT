import turtle
bgg = input("What bg colour do you want: ")
screen = turtle.Screen()
screen.bgcolor(bgg)
t = turtle.Turtle()
ck = 2
while ck > 1:

    # radius of the circle
    r = int(input("What Radius do you want for the rings: "))
    n = int(input("How many Rings do you want: "))
    c = input("What colour do you wanna use: ")
    p = int(input("Where would you like to start the rings (X value): "))
    pi = int(input("Where would you like to start the rings (Y value): "))
    nn = n + 1
    t.pencolor(c)
    t.up()
    t.sety(pi)
    t.setx(p)
    t.down()
    # Loop for printing concentric circles

    for i in range(nn):
        t.circle(r * i)
        t.up()
        t.sety((r * i)*(-1))
        t.down()

    pmpt = int(
        input("Do you want to draw another? (Enter 1 if yes,enter 2 if no): "))
    if pmpt == 1:
        pass
    elif pmpt == 2:
        ck = ck - 2
        print("Thank you for drawing! Click to exit. ")
        turtle.Screen().exitonclick
    else:
        print("That is not an option")
        continue
