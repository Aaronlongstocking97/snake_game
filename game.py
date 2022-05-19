"""
 Program:
    CS241 Assignment 11, Asteroids Project
 Instructor:
    Borther Macbeth
 Author:
    Aaron Jones
 Summary:
    This class handles all the game callbacks and interactions.
    It assumes the following classes exist:
        - Ship
        - Asteroid (and it's sub-classes)
        - Point
        - Velocity
        - Bullet
    This class will then call the appropriate functions of
    each of the above classes.

                     
"""

from global_ import *
import arcade
from bullet import Bullet
from asteroid import Asteroid
from ship import Ship
from large_asteroid import LargeAsteroid
from medium_asteroid import MediumAsteroid
from small_asteroid import SmallAsteroid

"""
* This class handles all the game callbacks and interaction
* This class will then call the appropriate functions of
* each of the above classes. Sets up the initial
* conditions of the game.
* :param width: Screen width
* :param height: Screen height
"""
class Game(arcade.Window):

    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.SMOKY_BLACK)
        self.ship = Ship()
        self.asteroids = [LargeAsteroid(), LargeAsteroid(), LargeAsteroid(),
                      LargeAsteroid(), LargeAsteroid()]
        self.held_keys = set()
        self.bullets = []

    """
    * Called automatically by the arcade framework.
    * Handles the responsibility of drawing all elements.
    """
    def on_draw(self):
        
        arcade.start_render()
        
        for bullet in self.bullets:
            bullet.draw()

        for asteroid in self.asteroids:
            asteroid.draw()
        
        if self.ship.alive == True:
            self.ship.draw()
        
    """
    * Update each object in the game.
    * :param delta_time: tells us how much time has actually elapsed
    """
    def update(self, delta_time):
        
        self.check_keys()
        self.check_collisions()
        self.ship.advance()
        
        for bullet in self.bullets:
            bullet.advance()
            
        for asteroid in self.asteroids:
            asteroid.advance()

    """
    * Checks to see if bullets have hit targets.
    * Updates scores and removes dead items.
    * :return:
    """
    def check_collisions(self):
        
        new_asteroid = []
        for bullet in self.bullets:
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius
                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                                abs(bullet.center.y - asteroid.center.y) < too_close):
                        bullet.alive = False
                        new_asteroid += asteroid.hit()
            self.asteroids += new_asteroid
        for asteroid in self.asteroids:
            if asteroid.alive and self.ship.alive:
                too_close = asteroid.radius + self.ship.radius
                if (abs(asteroid.center.x - self.ship.center.x) < too_close and
                    abs(asteroid.center.y - self.ship.center.y) < too_close):
                   self.ship.alive = False
                   
        self.cleanup_zombies()

    """
    * Removes any dead bullets or asteroids from the list.
    * :return:
    """
    def cleanup_zombies(self):
        
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:
            if not asteroid.alive:
                self.asteroids.remove(asteroid)

            
    """
    * This function checks for keys that are being held down.
    """
    def check_keys(self):

        if arcade.key.LEFT in self.held_keys:
            self.ship.rotate_left()

        if arcade.key.RIGHT in self.held_keys:
            self.ship.rotate_right()

        if arcade.key.UP in self.held_keys:
            self.ship.increase_speed()

        if arcade.key.DOWN in self.held_keys:
            self.ship.move_down()
            
        if arcade.key.SPACE in self.held_keys:
            pass

    """
    * Puts the current key in the set of keys that are being held.
    """
    def on_key_press(self, key: int, modifiers: int):
        
        if self.ship.alive:
            self.held_keys.add(key)
        
            if key == arcade.key.SPACE:
                bullet = Bullet(self.ship)
                bullet.fire()
                bullet.advance()
                self.bullets.append(bullet)

    """
    * Removes the current key from the set of held keys.
    """
    def on_key_release(self, key: int, modifiers: int):
        
        if key in self.held_keys:
            self.held_keys.remove(key)
    
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()