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
speed_x = 5
speed_y = 5

last = 'left'
finish = False

font.init()
font1 = font.SysFont('Arial', 70)
win_label = font1.render('Game over.', True, (255, 255, 255))
font2 = font.SysFont('Arial', 40)
label_left = font2.render('Player left wins!', True, (0, 255, 0))
label_right = font2.render('Player Right wins!', True, (255, 255, 0))

while game:
    window.fill((200, 200, 255))
    if not finish:
        pressed_keys = key.get_pressed()
        if pressed_keys[K_w] and player_left.rect.y > 0:
            player_left.rect.y -= 12
        if pressed_keys[K_s] and player_left.rect.y < 600:
            player_left.rect.y += 12
        if pressed_keys[K_UP] and player_right.rect.y > 0:
            player_right.rect.y -= 12
        if pressed_keys[K_DOWN] and player_right.rect.y < 600:
            player_right.rect.y += 12
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y >= 700 or ball.rect.y <= 0:
        speed_y *= -1
    if sprite.collide_rect(player_left, ball):
        last = 'left'
        speed_x *= -1
    if sprite.collide_rect(player_right, ball):
        last = 'right'
        speed_x *= -1
    if ball.rect.x < -100 or ball.rect.x > 900:
        finish = True
    if finish:
        window.blit(win_label, (300, 200))
        if last == 'left':
            window.blit(label_left, (340, 300))
        else:
            window.blit(label_right, (320, 300))
    for e in event.get():
        if e.type == QUIT:
            game = False

    player_left.draw()
    player_right.draw()
    ball.draw()
    display.update()
    timer.tick(60)
