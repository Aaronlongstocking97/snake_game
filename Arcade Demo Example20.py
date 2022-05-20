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
import random

BALL_RADIUS = 10
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
MOVE_AMOUNT = 5

class Ball:
    
    def __init__(self):
        ##
        self.box = Box()
        self.box.y = random.randrange(50, 250)
        self.box.x = 10
        self.dx = 3
        self.dy = 3
        ## override or overloading the constructor.
        


    def draw(self):
        
        arcade.draw_circle_filled(self.box.x, self.box.y, BALL_RADIUS, arcade.color.BLACK)
      
      
    def bounce_horizontal(self):
        ##   Think about the relationship between the Pong and Ball
        ##   what really does the bounce_horizontal function do?
        ##   Where they send this instrcution to make the ball bounce?
        if self.box.x < 0:
            self.dx = 3

    def bounce_vertical(self):
        
        if self.box.y > SCREEN_HEIGHT - BALL_RADIUS:
            self.dy = -3
        if self.box.y < BALL_RADIUS:
            self.dy = 3
            
    def advance(self):
        
        self.box.x += self.dx
        self.box.y += self.dy
            
class Box:
    
    def __init__(self):
        self.x = 390
        self.y = 150

        
    def draw(self):
        #arcade.draw_rectangle_filled(X-Cordinate, Y-Cordinate, Width, Height, arcade.color)
        arcade.draw_rectangle_filled(self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT, arcade.color.AIR_FORCE_BLUE)
        
        
class DemoApp(arcade.Window):
    """
    This class defines the demo application.
    It produces a rectangle on the screen.
    """
    
    def __init__(self, width, height):
        super().__init__(width, height)
        
        arcade.set_background_color(arcade.color.WHITE)
        
        self.ball = Ball()
        self.box = Box()
        self.holding_left = False
        self.holding_right = False
        
    def on_draw(self):
        """
        Called every time we need to draw the window
        """
        
        arcade.start_render()
        self.ball.draw()
        self.box.draw()
        
    def move_up(self):
        
        if self.box.y < 275:
            self.box.y += MOVE_AMOUNT
            self.holding_left = False
        
    def move_down(self):
        
        if self.box.y >= 25:
            self.box.y -= MOVE_AMOUNT
            self.holding_right = False
        
        
    def check_keys(self):
        """
        Checks to see if the user is holding down an
        arrow key, and if so, takes appropriate action.
        """
        if self.holding_left:
            self.move_down()

        if self.holding_right:
            self.move_up()

    def on_key_press(self, key, key_modifiers):
        """
        Called when a key is pressed. Sets the state of
        holding an arrow key.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = True

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = True

    def on_key_release(self, key, key_modifiers):
        """
        Called when a key is released. Sets the state of
        the arrow key as being not held anymore.
        :param key: The key that was pressed
        :param key_modifiers: Things like shift, ctrl, etc
        """
        if key == arcade.key.LEFT or key == arcade.key.DOWN:
            self.holding_left = False

        if key == arcade.key.RIGHT or key == arcade.key.UP:
            self.holding_right = False
  
          
    def update(self, delta_time):
        """
        The purpose of this method is to move everything
        """
        self.ball.advance()
        self.check_keys()
        self.check_bounce()
        
    def check_bounce(self):
        """
        Checks to see if the ball has hit the borders
        of the screen and if so, calls its bounce methods.
        """
        if self.ball.box.x < 0 and self.ball.dx < 0:
            self.ball.bounce_horizontal()

        if self.ball.box.y < 0 and self.ball.dy < 0:
            self.ball.bounce_vertical()

        if self.ball.box.y > SCREEN_HEIGHT and self.ball.dy > 0:
            self.ball.bounce_vertical()
        
window = DemoApp(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
        
        
        
        
        