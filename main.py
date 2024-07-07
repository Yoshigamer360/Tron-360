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
    def __init__(self, x, y, bearing , colour):
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

# Set up the game window
width, height = 600,660
offset = height - width
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tron by Yoshi_Gamer_360")

# Font and clock
font = pygame.font.SysFont("Centaur", 72)
clock = pygame.time.Clock()
checkTime = time.time()

# Define players and paths of players
objects = list()
path = list()
p1, p2 = newGame()
objects.append(p1)
objects.append(p2)
path.append((p1.rect, '1'))
path.append((p2.rect, '2'))

# Score
playerScore = [0, 0]

# Create walls and wall array
wallRects = [
    pygame.Rect([0, offset, 15, height]),
    pygame.Rect([0, offset, width, 15]),
    pygame.Rect([width - 15, offset, 15, height]),
    pygame.Rect([0, height - 15, width, 15])]

# Game state
done = False
new = False

# Game play loop
while not done:
    # Loop over all events happening in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Player 1 controls
            if event.key == pygame.K_w:
                objects[0].bearing = (0, -2)
            elif event.key == pygame.K_s:
                objects[0].bearing = (0, 2)
            elif event.key == pygame.K_a:
                objects[0].bearing = (-2, 0)
            elif event.key == pygame.K_d:
                objects[0].bearing = (2, 0)
            # Player 2 controls
            if event.key == pygame.K_UP:
                objects[1].bearing = (0, -2)
            elif event.key == pygame.K_DOWN:
                objects[1].bearing = (0, 2)
            elif event.key == pygame.K_LEFT:
                objects[1].bearing = (-2, 0)
            elif event.key == pygame.K_RIGHT:
                objects[1].bearing = (2, 0)
                    
    screen.fill(colourBackground)

    # Render the walls
    for r in wallRects:
        pygame.draw.rect(screen, colourWalls, r, 0)

    # Loop over players
    for obj in objects:
        if (obj.rect, '1') in path or (obj.rect, '2') in path or \
           obj.rect.collidelist(wallRects) > -1:
            if (time.time() - checkTime) >= 0.1:
                checkTime = time.time()
                if obj.colour == colourPlayer1:
                    playerScore[1] += 1
                else:
                    playerScore[0] += 1
                new = True
                newP1, newP2= newGame()
                objects = [newP1, newP2]
                path = [(p1.rect, '1'), (p2.rect, '2')]
                break
        else:
            if obj.colour == colourPlayer1:
                path.append((obj.rect, '1'))
            else:
                path.append((obj.rect, '2'))
        obj.draw()
        obj.move()

    # Loop over the paths and render them
    for rect in path:
        if new is True:
            path = []
            new = False
            break
        if rect[1] == '1':
            pygame.draw.rect(screen, colourPlayer1, rect[0], 0)
        else:
            pygame.draw.rect(screen, colourPlayer2, rect[0], 0)

    # Render the score text
    scoreText = font.render(f"{playerScore[0]} : {playerScore[1]}",
                             True, colourText)
    scoreTextRect = scoreText.get_rect()
    scoreTextRect.centerx = int(width/2)
    scoreTextRect.centery = int(offset/2)
    screen.blit(scoreText, scoreTextRect)
    
    # Update the current frame
    pygame.display.flip()
    # Set the frame rate (speed)
    clock.tick(60)

pygame.quit()
