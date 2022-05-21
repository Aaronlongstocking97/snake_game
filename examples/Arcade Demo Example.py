"""
 Program:
    CS241 Checkpoint 05A, 
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary: 
    
                     
"""

import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400

class Box:
    
    def __init__(self):
        self.x = 100
        self.y = 100
        
        self.a = 175
        self.b = 175
        
        self.c = 100
        self.d = 100
        
        self.dx = 3
        self.ca = 3
        self.xy = 3
        
    def draw(self):
        #arcade.draw_rectangle_filled(X-Cordinate, Y-Cordinate, Width, Height, arcade.color)
        arcade.draw_rectangle_filled(self.x, self.y, 70, 20, arcade.color.AIR_FORCE_BLUE)
        arcade.draw_rectangle_filled(self.a, self.b, 70, 20, arcade.color.RED)
        arcade.draw_rectangle_filled(self.c, self.d, 20, 70, arcade.color.GREEN)
        
    def advanceBlue(self):
        if self.x > SCREEN_WIDTH:
            self.dx = -3
        if self.x < 0:
            self.dx = 3
        
        self.x += self.dx
        
    def advanceRed(self):
        if self.a > SCREEN_WIDTH:
            self.ca = -3
        elif self.a < 0:
            self.ca = 3
            
        self.a += self.ca
        
    def advanceGreen(self):
        if self.d > SCREEN_HEIGHT:
            self.xy = -3
        elif self.d < 0:
            self.xy = 3
            
        self.d += self.xy
        
class DemoApp(arcade.Window):
    """
    This class defines the demo application.
    It produces a rectangle on the screen.
    """
    
    def __init__(self, width, height):
        super().__init__(width, height)
        
        arcade.set_background_color(arcade.color.WHITE)
        
        self.box = Box()
        
    def on_draw(self):
        """
        Called every time we need to draw the window
        """
        
        arcade.start_render()
        
        self.box.draw()
        
    def update(self, delta_time: float):
        """
        The purpose of this method is to move everything
        """
        self.box.advanceBlue()
        self.box.advanceRed()
        self.box.advanceGreen()
        
window = DemoApp(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
        
        
        
        
        