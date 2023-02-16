import turtle, random

SCALE = 32 #Controls how many pixels wide each grid square is

class Game:
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)

        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        self.occupied = []
        temp = []
        for i in range(21):
            for j in range(11):
                temp.append(False)
            self.occupied.append(temp)
            temp = []
        
        turtle.ontimer(self.gameloop, 300)
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        #These three lines must always be at the BOTTOM of __init__
        print(self.occupied)
        self.active = Block()
        turtle.update()
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        if self.active.valid(0,-1, self.occupied):
            self.active.move(0,-1)
        else:
            for i in self.active.squares:
                if i.ycor() < 20 and i.ycor() >= 0:
                    self.occupied[i.ycor()][i.xcor()] = True
            self.active = Block()
        turtle.update()
        turtle.ontimer(self.gameloop, 300)
    def move_left(self):
        if self.active.valid(0,-1, self.occupied):
            self.active.move(-1, 0)
        turtle.update()
    def move_right(self):
        if self.active.valid(0,-1, self.occupied):
            self.active.move(1, 0)
        turtle.update()
       
class Square(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
        self.goto(x,y)

class Block():
    def __init__(self):
        self.squares = []
        sq1 = Square(3,21,'cyan')
        sq2 = Square(4,21,'cyan')
        sq3 = Square(5,21,'cyan')
        sq4 = Square(6,21,'cyan')
        self.squares.append(sq1)
        self.squares.append(sq2)
        self.squares.append(sq3)
        self.squares.append(sq4)
    def move(self, dx, dy):
        for i in self.squares:
            i.goto(i.xcor()+dx,i.ycor()+dy)
    def valid(self, dx, dy, lst):
        for i in self.squares:
            if i.xcor()+dx < 0 or i.xcor()+dx > 9:
                return False
            elif i.ycor() + dy < 20 and lst[i.ycor()+dy][i.xcor()+dx] == True:
                return False
        return True    
if __name__ == '__main__':
    Game()
    
