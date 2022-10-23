import turtle

def askInput(t, str):
    return t.textInput("Slotmachine", str)

def writeText(str):
    ttext = turtle.Turtle() 
    ttext.hideturtle()
    ttext.color("white")
    ttext.write(str, align="center", font=("Verdana", 24, "bold"))

def drawSlots(symbolsLst): 
    t = turtle.Turtle()
    t.hideturtle()
    window = turtle.Screen()
    window.bgcolor("black")
    t.color("red")
    t.speed(200)
    turtle.width(14)
    t.up()  
    t.goto(-300, 200)  
    t.down()  
    draw3squares(t, 100, symbolsLst)
    window.exitonclick()

def draw3squares(t, length, symbolsLst):
    for i in range(3):
        t.color("red")
        drawSquare(t, length)
        t.up()  

        # go to the "enter" of the square (not quite center but for the letter to be centered)
        t.left(90)
        t.forward(length/3)
        t.left(-90)
        t.forward(length/2)

        # write the symbol
        t.down()
        t.color("black")
        t.write(symbolsLst[i], align="center", font=("Verdana", 24, "normal"))
        t.up()  

        # go back
        t.forward(length/2)
        t.left(-90)
        t.forward(length/3)
        t.left(90)
        t.forward(5) 
        t.down()

def drawSquare(t, length):
    t.fillcolor("red")
    t.begin_fill()
  
    t.forward(length)
    t.left(90)
    
    t.forward(length)
    t.left(90) 
    
    t.forward(length)
    t.left(90)
    
    t.forward(length) 
    t.left(90)
    
    t.end_fill()
