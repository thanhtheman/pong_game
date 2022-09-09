from string import whitespace
import pygame

pygame.init()

screen_width, screen_height = 700, 500

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

fps = 60
white =(255, 255, 255)
black = (0, 0, 0)

class Paddle:
    def __init__(self, x, y, paddle_width, paddle_height):
        self.x = x
        self.y = y
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height


def draw(win):
    win.fill(black)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)
        draw(game_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
    pygame.quit()

if __name__ == '__main__':
    main()