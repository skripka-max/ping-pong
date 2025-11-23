from pygame import *
window = display.set_mode((900, 800))
display.set_caption('ping-pong')
timer = time.Clock()
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, file_name, x, y, width = 30, height = 200):
        self.image = transform.scale(image.load(file_name), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_left = GameSprite('player-left.png', 5, 300)
player_right = GameSprite('player-right.png', 865, 300)
ball = GameSprite('ball.png', 400, 350, width = 100, height = 100)

while game:
    window.fill((200, 200, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    player_left.draw()
    player_right.draw()
    ball.draw()
    display.update()
    timer.tick(60)
