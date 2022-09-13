import pygame

pygame.init()

screen_width, screen_height = 700, 500

game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

fps = 60
white =(255, 255, 255)
black = (0, 0, 0)

paddle_width, paddle_height = 20, 100
ball_radius = 7

score_font = pygame.font.SysFont('comicsans', 50)


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

class Ball:
    max_velocity = 5
    color = white

    def __init__(self, x, y, radius):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_velocity = self.max_velocity
        self.y_velocity = 0

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, ((self.x, self.y)), self.radius)
    
    def move(self):
        self.x += self.x_velocity
        self.y += self.y_velocity
    
    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.y_velocity = 0
        self.x_velocity *= -1



def draw(win, paddles, ball, left_score, right_score):
    win.fill(black)

    left_score_text = score_font.render(f'{left_score}', 1, white)
    right_score_text = score_font.render(f'{right_score}', 1, white)
    win.blit(left_score_text, (screen_width // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (screen_width * (3/4) - right_score_text.get_width() // 2, 20))

    # this draw method is actually from the class paddle, not the general draw method
    for paddle in paddles:
        paddle.draw(game_screen)
    
    for i in range(10, screen_height, screen_height//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, white, (screen_width//2 - 5, i, 5, screen_width//20))
    
    ball.draw(game_screen)

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

def handle_collision(ball, left_paddle, right_paddle):

    if ball.y + ball_radius >= screen_height:
        ball.y_velocity *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_velocity *= -1

    if ball.x_velocity < 0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + paddle_height:
            if ball.x - ball.radius <= left_paddle.x + paddle_width:
                ball.x_velocity *= -1

                # dealing with the y bouncing direction, d = difference between center paddle (middle_y) - ball.y
                middle_y = left_paddle.y + paddle_height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (paddle_height / 2) / ball.max_velocity
                collision_y_velocity = difference_in_y / reduction_factor
                ball.y_velocity = -1 * collision_y_velocity
    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + paddle_height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_velocity *= -1

                middle_y = right_paddle.y + paddle_height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (paddle_height / 2) / ball.max_velocity
                collision_y_velocity = difference_in_y / reduction_factor
                ball.y_velocity = -1 * collision_y_velocity


def main():
    run = True
    clock = pygame.time.Clock()
    #creating the paddle
    left_paddle = Paddle(10, screen_height//2 - paddle_height//2, paddle_width, paddle_height)
    right_paddle = Paddle(screen_width - 10 - paddle_width, screen_height//2 - paddle_height//2, paddle_width, paddle_height)
    ball = Ball(screen_width//2, screen_height//2, ball_radius)
    left_score = 0
    right_score = 0

    while run:
        # how fast the loop should run
        clock.tick(fps)
        
        # drawing the screen, the paddle
        draw(game_screen, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        #key pressed
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        #moving the ball
        ball.move()

        #hanlding the collision
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x > screen_width:
            left_score += 1
            ball.reset()
        elif ball.x < 0:
            right_score += 1
            ball.reset()
        
        




    pygame.quit()

if __name__ == '__main__':
    main()