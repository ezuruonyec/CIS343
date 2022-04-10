#!/usr/bin/env python3

import pygame as pg
from pygame import *
import random

"""
A constructor that creates a brick

"""
class Brick(pg.sprite.Sprite):
    def __init__(self, xcoord, ycoord):
        super().__init__()
        
        r = random.randint

        self.image = pg.Surface((100, 50))
        self.rect = self.image.get_rect()
        self.image.fill( (r(0, 255), r(0, 101), r(0, 164)) )
        
        

        #pg.draw.circle(self.image, (0, 101, 164), (32, 32), 32)
        self.rect.x = xcoord
        self.rect.y = ycoord

        # add methods for health/hit

"""
A constructor that creates a ball
"""
class Ball(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((15, 15))

        self.rect = self.image.get_rect()
        
        self.rect.x = 400
        self.rect.y = 300

"""
The paddle class
"""
class Paddle(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # create paddle
        self.image = pg.Surface((300, 25))
        self.rect = self.image.get_rect()
        

        # position paddle
        self.rect.x = 400
        self.rect.y = 575

        # set initial velocity
        self.velocity = 5

    def move(self):
        """
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    print(pygame.key.name(event.key))
        """
        keys = pg.key.get_pressed()

        self.rect.x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 5
        self.rect.y += (keys[pg.K_LEFT] - keys[pg.K_RIGHT]) * 5

        if self.rect.x > 550:
            self.rect.x = 545
        if self.rect.x < 0:
            self.rect.x = 5


class Blah(pg.sprite.Sprite):
    explodifiers = None
    def __init__(self):
        super().__init__()
        r = random.randint
        self.image = pg.Surface((r(0,64),r(0,64)))
        self.image.fill( (r(0,255), r(0,101), r(0,164)) )
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,800)
        self.rect.y = random.randint(0,600)
        self.velocity = [r(0,3) - 3, r(0,3) - 3]
        self.explodifiers = None
#        self.boom = pg.mixer.Sound("./boom.mp3")

    def update(self):
        keys = pg.key.get_pressed()

        self.rect.x += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 5
        self.rect.y += (keys[pg.K_LEFT] - keys[pg.K_RIGHT]) * 5

        if self.rect.x > 550:
            self.rect.x = 545
        if self.rect.x < 0:
            self.rect.x = 5
#         self.boom.play()

    def setExplodifiers(self, explodifiers):
        self.explodifiers = explodifiers




class Game:
    def __init__(self):
        pg.init()
        self.__running = False
        self.screen = pg.display.set_mode( (800, 600) )
        self.clock = pg.time.Clock()
        self.blahs = pg.sprite.Group()
        self.exploders = pg.sprite.Group()
        self.brick = pg.sprite.Group()
        self.paddles = pg.sprite.Group()

    def run(self):
        while self.__running:
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.__running = False
                    pg.quit()
                    exit()
            # Take events

            # Update updateable objects
            self.blahs.update()
            # self.paddles.move()
            # Redraw
            self.screen.fill( (255, 255, 255) )
            self.blahs.draw(self.screen)
            self.exploders.draw(self.screen)
            self.paddles.draw(self.screen)
            pg.display.flip()
            self.clock.tick(60)

    def setRunning(self, running):
        self.__running = running

    def addBrick(self, brick):
        self.brick.add(brick)

    def addBlah(self, blah):
        self.blahs.add(blah)

    def addExplodifier(self, exploder):
        self.exploders.add(exploder)

    def getExplodifiers(self):
        return self.exploders

    def getPaddle(self):
        return self.paddles



def main():
    game = Game()

    for x in range(0, 8):
        for y in range(0, 5):
            game.addExplodifier(Brick(x * 100, y * 50))
        #game.addBlah( Blah() )

    game.addExplodifier(Paddle())
    game.addExplodifier(Ball())
    Blah.explodifiers = game.getExplodifiers()
    game.setRunning(True)
    game.run()

if __name__ == '__main__':
    main()

