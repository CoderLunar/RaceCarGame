import pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 800
FONT = pygame.font.SysFont("comicsans", 60)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Game!")

WHITE = (255, 255, 255)
FPS = 60
VEL = 3
RACECAR_WIDTH, RACECAR_HEIGHT = (110, 50)

GRASS_IMAGE = pygame.image.load(os.path.join('Assets', 'grass_background.png'))
GRASS = pygame.transform.scale(GRASS_IMAGE, (900, 800))
RACETRACK_IMAGE = pygame.image.load(os.path.join('Assets', 'racetrack.png'))
RACETRACK = pygame.transform.scale(RACETRACK_IMAGE, (900, 800))
PURPLE_CAR_IMAGE = pygame.image.load(os.path.join('Assets', 'purple_racecar.png'))
PURPLE_CAR = pygame.transform.scale(PURPLE_CAR_IMAGE, (160, 60))
YELLOW_CAR_IMAGE = pygame.image.load(os.path.join('Assets', 'yellow_racecar.png'))
YELLOW_CAR = pygame.transform.scale(YELLOW_CAR_IMAGE, (RACECAR_WIDTH, RACECAR_HEIGHT))
PURPLE_CAR_LEFT = pygame.transform.rotate(PURPLE_CAR, 180)
PURPLE_CAR_UP = pygame.transform.rotate(PURPLE_CAR, 270)

def draw_window(purple, yellow):
    WIN.fill(WHITE)
    WIN.blit(GRASS, (0, 0))
    WIN.blit(RACETRACK, (0, 0))
    WIN.blit(PURPLE_CAR, (purple.x, purple.y))
    WIN.blit(YELLOW_CAR, (yellow.x, yellow.y))

    pygame.display.update()

def handle_purple_movement(keys_pressed, purple):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        purple.x -= VEL
    if keys_pressed[pygame.K_d]:
        purple.x += VEL
    if keys_pressed[pygame.K_w]:
        purple.y -= VEL
    if keys_pressed[pygame.K_s]:
        purple.y += VEL

def handle_yellow_movement(keys_pressed, yellow):
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:
        yellow.x += VEL
    if keys_pressed[pygame.K_UP]:
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN]:
        yellow.y += VEL

def main():
    purple = pygame.Rect(130, 60, 160, 60)
    yellow = pygame.Rect(280, 60, RACECAR_WIDTH, RACECAR_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        handle_purple_movement(keys_pressed, purple)
        handle_yellow_movement(keys_pressed, yellow)
        draw_window(purple, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()
