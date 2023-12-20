import pygame

pygame.init()

win_w = 600
win_h = 500
FPS = 40

class Pers:
    def __init__(self, x, y, w, h, image, speed):
        self.rect = pygame.Rect(x, y, w, h)
        image = pygame.transform.scale(image, (w, h))
        self.image = image
        self.speed = speed

    def move(self, key_left, key_right, key_up, key_down):
        k = pygame.key.get_pressed()
        if k[key_right]:
            if self.rect.right <= win_w:
                self.rect.x += self.speed 
        elif k[key_left]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
        elif k[key_up]:
            if self.rect.y >= 0:
                self.rect.y -= self.speed
        elif k[key_down]:
            if self.rect.bottom <= win_h:
                self.rect.y += self.speed
        
    
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = pygame.display.set_mode((win_w, win_h))
pygame.display.set_caption("Догонялки")
clock = pygame.time.Clock()
#window.fill((2, 200, 200))

background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (win_w, win_h))
window.blit(background, (0, 0))

pers_img = pygame.image.load("sprite1.png")
pers1_img = pygame.image.load("sprite2.png")
pers1 = Pers(250, 250, 50, 50, pers_img, 5)
pers2 = Pers(150, 50, 50, 50, pers1_img, 5)

game = True
while game:
    window.blit(background, (0, 0))
    
    pers1.move(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s)
    pers1.update()
    pers2.move(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN)
    pers2.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)

