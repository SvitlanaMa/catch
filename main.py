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

    def move(self):
        k = pygame.key.get_pressed()
        if k[pygame.K_d]:
            if self.rect.right <= win_w:
                self.rect.x += self.speed 
        elif k[pygame.K_a]:
            if self.rect.left >= 0:
                self.rect.x -= self.speed
        elif k[pygame.K_w]:
            self.rect.y -= self.speed
        elif k[pygame.K_s]:
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
pers1 = Pers(250, 250, 50, 50, pers_img, 5)

game = True
while game:
    window.blit(background, (0, 0))
    
    pers1.move()
    pers1.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    pygame.display.update()
    clock.tick(FPS)

