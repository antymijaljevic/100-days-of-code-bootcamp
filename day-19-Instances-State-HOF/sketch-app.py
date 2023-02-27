from turtle import Turtle, Screen

class SketchApp:
    """ sketch application """
    def __init__(self):
        self.tim = Turtle()
        self.screen = Screen()
        self.tim.speed("fastest")
        self.clock = 0
        
    def forward(self):
        self.tim.forward(10)
    
    def backwards(self):
        self.tim.backward(10)
        
    def counter_clockwise(self):
        self.tim.setheading(self.clock)
        self.clock += 5  
        
    def clockwise(self):
        self.tim.setheading(self.clock)
        self.clock -= 5
        
    def clear_screen(self):
        """
            clear screen and return mouse 
            to the starting position
        """
        self.tim.clear()
        self.tim.penup()
        self.tim.home()
        self.tim.pendown()
        
    def start(self):
        """ start the game """
        # key listener
        self.screen.listen()
        
        # possible keys/moves
        self.screen.onkey(fun=self.forward, key="w")
        self.screen.onkey(fun=self.backwards, key="s")
        self.screen.onkey(fun=self.counter_clockwise, key="a")
        self.screen.onkey(fun=self.clockwise, key="d")
        self.screen.onkey(fun=self.clear_screen, key="c")
        
        # exit on mouse click
        self.screen.exitonclick()
        
sketch_app = SketchApp()
sketch_app.start()
