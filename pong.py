from string import whitespace
from turtle import up
import pygame

pygame.init()

screen_width, screen_height = 700, 500

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

fps = 60
white =(255, 255, 255)
black = (0, 0, 0)

paddle_width, paddle_height = 20, 100

class Paddle:
    color = white
    velocity = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.velocity
        else:
            self.y += self.velocity

def draw(win, paddles):
    win.fill(black)

    # this draw method is actually from the class paddle, not the general draw method
    for paddle in paddles:
        paddle.draw(game_screen)

    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.velocity >= 0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.velocity + paddle_height <= screen_height:
        left_paddle.move(up=False)
    if keys[pygame.K_UP] and right_paddle.y - right_paddle.velocity >= 0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.velocity + paddle_height <= screen_height:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()
    #creating the paddle
    left_paddle = Paddle(10, screen_height//2 - paddle_height//2, paddle_width, paddle_height)
    right_paddle = Paddle(screen_width - 10 - paddle_width, screen_height//2 - paddle_height//2, paddle_width, paddle_height)

    while run:
        # how fast the loop should run
        clock.tick(fps)
        
        # drawing the screen, the paddle
        draw(game_screen, [left_paddle, right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        #key pressed
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()