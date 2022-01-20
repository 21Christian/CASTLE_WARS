import pygame

# Initialization of the game
pygame.init()

# Title and icon
pygame.display.set_caption("Castle Wars")
icon = pygame.image.load("castle.png")
pygame.display.set_icon(icon)

# Screen
screen = pygame.display.set_mode((1200, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((250, 250, 225))
        pygame.display.update()
