import pygame
from random import randint

pygame.init()

WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bee and Flowers")

bee_img = pygame.image.load("Lesson 6 homework/images/bee.png")
flower_img = pygame.image.load("Lesson 6 homework/images/flower.png")
bg_img = pygame.transform.scale(pygame.image.load("Lesson 6 homework/images/bg.png"), (WIDTH, HEIGHT))

bee_rect = bee_img.get_rect(topleft=(randint(0, WIDTH - 50), randint(0, HEIGHT - 50)))
flower_rect = flower_img.get_rect(topleft=(randint(0, WIDTH - 50), randint(0, HEIGHT - 50)))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 40)
message = ""
score = 0
def place_flower():
    flower_rect.topleft = (randint(0, WIDTH - flower_rect.width), randint(0, HEIGHT - flower_rect.height)) #random position

running = True
while running:
    screen.blit(bg_img, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if flower_rect.collidepoint(event.pos):
                score += 10
                message = "Good job!"
                place_flower()
            else:
                message = "Try again!"

    screen.blit(flower_img, flower_rect)
    screen.blit(bee_img, bee_rect)
    screen.blit(font.render("Score:"+str(score), True, BLACK),(300,250))
    screen.blit(font.render(message,True, BLACK), (300,250))

    pygame.display.flip()

pygame.quit()

    