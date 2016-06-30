import os
import random
import pygame

# Class for the orange dude
class Player(object):

    def __init__(self):
        self.rect = pygame.Rect(30, 30, 10, 10)

    def move(self, dx, dy):

        # Move each axis separately. Note that tddddddhis checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):

        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

# Nice class to hold a wall rect
class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

# Set up the display
pygame.display.set_caption("Get to the red square!")
screen = pygame.display.set_mode((890, 500))

clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player
player1 = Player() # Create the player
player2 = Player() # Create the player
player3 = Player() # Create the player
# Holds the level layout in a list of strings.
level = [
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W       E           WWWWWWWWWWWWWW             WWWWWWWWWW",
"WW     WWWWWW                                WWWWWWWWWW"
"W   WWWW       WWWWWWWWWWWWWWWWWWWWW WWWWWWWWWWWWWWWWWWW",
"W   W        WWWW                             WWWWWWWWWW",
"W WWW  WWWW                                   WWWWWWWWWW",
"W   W     W W      WWWWWWWW                           W",
"W   W     W   WWW                            WWWWWWW  W",
"W   WWW WWW   W W WWWWWWWWWWWWWW  WWWWW  WWWWWWWWWWW  W",
"W     W   W   W WWWWWWWWW                             W",
"WWW   W   W WWW WWWWWWWWW WWWWWWWWWWWWWWWW WWWWWWWW   W",
"W W      WW          WWWWWW                    WWWW   W",
"W W   WWWW   WWWWWWW        WWWWWWWWWWWWWW WWWWWWWW   WW",
"W     W              WWWW                       WWWW  WW",
"W                                                     W",
"WWWWWWWWWWWWWW  WWWWWWWWWWWWWWWWWWW WWWWWWWWWWWWWWWW WWW",
"W                                                    W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",





]

# Parse the level string above. W = wall, E = exit
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)

    if key[pygame.K_a]:
        player1.move(-2, 0)
    if key[pygame.K_d]:
        player1.move(2, 0)
    if key[pygame.K_w]:
        player1.move(0, -2)
    if key[pygame.K_s]:
        player1.move(0, 2)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    (player2_x, player2_y) = player2.rect.center
    dx = mouse_x - player2_x
    dy = mouse_y - player2_y
    player2.move(dx, dy)


    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        raise SystemExit,sound.play()
        print "You win Wiktor!"
    if player1.rect.colliderect(end_rect):
        raise SystemExit, "You win piotrek!"
    if player2.rect.colliderect(end_rect):
        raise SystemExit, "You win! "


    # Draw the scenea
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 0, 200), player1.rect)
    pygame.draw.rect(screen, (0, 255 ,0 ), player2.rect)

    pygame.mixer.init()
    sound = pygame.mixer.Sound('dzwiek/fanfary.wav')
    pygame.mixer.init()
    sound = pygame.mixer.Sound('dzwiek/fanfary.wav')

    pygame.display.flip()