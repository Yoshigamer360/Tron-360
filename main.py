# A remake of the classic arcade game Tron
# Date 04/07/24
# Created by: Yoshi Gamer 360

# Player 1 uses WASD to move
# Player 2 uses arrow keys to move

# Libraries
import pygame, time

# Start game engine
pygame.init()

# Define colour variables
colourBackground = (1, 4, 59)
colourPlayer1 = (0, 255, 17)
colourPlayer2 = (255, 234, 0)
colourWalls = (0, 1, 10)
colourText = (221, 222, 240)

# Player class
class Player:
    def __init__(self, x, y , bearing , colour):
        self.x = x
        self.y = y
        self.bearing = bearing
        self.colour = colour
        self.speed = 1
        self.rect = pygame.Rect(self.x -1, self.y -1, 2, 2)

    def draw(self):
        self.rect = pygame.Rect(self.x -1, self.y -1, 2, 2)
        pygame.draw.rect(screen, self.colour, self.rect, 0)

    def move(self):
        self.x += self.bearing[0]
        self.y += self.bearing[1]

# New game function - to create players
def newGame():
    newP1 = Player(50, height / 2, (2, 0), colourPlayer1)
    newP2 = Player(width - 50, height / 2, (-2, 0), colourPlayer2)
    return newP1, newP2
