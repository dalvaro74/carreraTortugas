import turtle

class Circuito():
    corredores = []
    __posStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red', 'blue', 'green', 'orange')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width,height)
        self.__screen.bgcolor('lightgrey')
        self.__startline = -width/2 +20
        self.__finishline = width/2 -20       
        self.__createRunners()
        
    def __createRunners(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.penup()
            new_turtle.setpos(self.__startline,self.__posStartY[i])
            self.corredores.append(new_turtle)
        
if __name__ == '__main__':
    circuito = Circuito(640,480)