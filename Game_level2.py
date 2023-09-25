# COMP 123
# Devi Naum
# Blake Kell
""" This file contains the necessary pygame code to run the second level of difficulty for the game."""
# import all the necessary modules, especially pygame and all the buttons needed to play from pygame.locals
from Game_level3 import *
import pygame
import random
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_r,
    K_w,
    K_s,
    K_a,
    K_d
)

def gameStart1():
    """This function is created in order for the 'practice' file to call this game when the user presses the 'Play the Game
    button. This is the sole function of creating this function."""
    SCREEN_WIDTH = 600   # Setting the width of the playing screen.
    SCREEN_HEIGHT = 650  # Setting the height of the playing screen.

    class Player(pygame.sprite.Sprite):
        """This class contains the player, a.k.a the Frog that will be the player in the game. In this class, we create
        the frog itself and we also set the buttons that will move it in the game."""
        def __init__(self):
            """ Creating the player with the photo of the frog and the place where the frog starts in the screen."""
            super(Player, self).__init__()
            self.surf = pygame.image.load("frog.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(center=(SCREEN_WIDTH/2,640))

        def update(self, pressed_keys):
            """ This function sets the keyboard buttons that will move the frog around the screen and where the frog
            is allowed to go and where it is not on the screen. Further, the area supposed to be reached by the frog (player)
            is set in this function. """
            if pressed_keys[K_UP]:
                self.rect.move_ip(0, -1)
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0, 1)
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-1, 0)
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(1, 0)
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -1)
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 1)
            if pressed_keys[K_a]:
                self.rect.move_ip(-1, 0)
            if pressed_keys[K_d]:
                self.rect.move_ip(1, 0)
            if pressed_keys[K_r]:
                gameStart1()

            if self.rect.left < 0:
                player.kill()
                pygame.time.wait(300)
                gameStart1()
            if self.rect.right > SCREEN_WIDTH:
                player.kill()
                pygame.time.wait(300)
                gameStart1()
            if self.rect.top <= 40:
                gameStart2()
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT

    class Enemy(pygame.sprite.Sprite):
        """This class creates the first enemy object which is the car. It sets the starting place and
        the finish line for this object."""
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.image.load("car_L.gif").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 40, SCREEN_WIDTH + 100),
                    random.randint(520, 565),
                )
            )
            self.speed = 2

        def update(self):
            """This function sets the speed of the car and at what point in the screen it will be removed."""
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    class Enemy1(pygame.sprite.Sprite):
        """This is the same function as above, just for the cars coming from the other direction."""
        def __init__(self):
            super(Enemy1, self).__init__()
            self.surf = pygame.image.load("car_R.gif").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(-20, -10),
                    random.randint(375, 420),
                )
            )
            self.speed = 2

        def update(self):
            """This function sets the speed of the car and at what point in the screen it will be removed."""
            self.rect.move_ip(self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    class Enemy2(pygame.sprite.Sprite):
        """This function creates the Crocodile enemy in the same way as before."""
        def __init__(self):
            super(Enemy2, self).__init__()
            self.surf = pygame.image.load("crocc-removebg-preview.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(SCREEN_WIDTH + 40, SCREEN_WIDTH + 100),
                    random.randint(85, 130),
                )
            )
            self.speed = 2

        def update(self):
            """This function sets the speed of the crocodile and at what point in the screen it will be removed."""
            self.rect.move_ip(-self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    class Enemy3(pygame.sprite.Sprite):
        """This function creates the Crocodile enemy in the same way as before."""
        def __init__(self):
            super(Enemy3, self).__init__()
            self.surf = pygame.image.load("crocc_L-removebg-preview.png").convert()
            self.surf.set_colorkey((0, 0, 0), RLEACCEL)
            self.rect = self.surf.get_rect(
                center=(
                    random.randint(-20, -10),
                    random.randint(240, 275),
                )
            )
            self.speed = 2

        def update(self):
            """This function sets the speed of the crocodile and at what point in the screen it will be removed."""
            self.rect.move_ip(self.speed, 0)
            if self.rect.right < 0:
                self.kill()

    pygame.mixer.init()  # Enables the music at first for the game.
    pygame.init()        # Initiates the game itself.

    clock = pygame.time.Clock()   # Allows us to set the game's frame rate later on.

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Creates the display per width and height.

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 800)  # Creates the event needed for us to add the multiple enemies popping up.

    player = Player()

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # pygame.mixer.music.load("Lofi_again.mp3")
    # pygame.mixer.music.play(loops=-1)

    running = True

    bg = pygame.image.load("background-easy2.png")

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            elif event.type == QUIT:
                running = False

            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                new_enemy1 = Enemy1()
                new_enemy2 = Enemy2()
                new_enemy3 = Enemy3()
                enemies.add(new_enemy, new_enemy1, new_enemy2, new_enemy3)
                all_sprites.add(new_enemy, new_enemy1, new_enemy2, new_enemy3)


        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)

        enemies.update()

        screen.blit(bg, (0, -70))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            """Important statement that kills the player in case of contact with the obstacles or 'enemies'."""
            player.kill()
            pygame.time.wait(30)
            gameStart1()

        pygame.display.flip()   # This very important function updates the display.

        clock.tick(130)   # Setting the game's frame rate.


    pygame.mixer.music.stop()   # Stops the music when the game ends.
    pygame.mixer.quit()
    exit()


""" This game was tested mainly with trial and error accross all three levels. For example, in the case of the frame
rate, I needed to use trial and error to adjust it accordingly to how the game is supposed to be and I couldn't test it
with Python functions. Another example would be the occurrences of the enemies coming from both sides as I need to 
adjust it to the game's style."""