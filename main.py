from pygame import *
window = display.set_mode((900, 800))
display.set_caption('ping-pong')
timer = time.Clock()
game = True

class Platform(sprite.Sprite):
    def __init__(self, file_name, x, y):
        self.image = image.load(file_name)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

while game:
    window.fill((200, 200, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    timer.tick(60)
