import pygame
import sys
import random


pygame.init()


window_size = (600, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Snake Game')


black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0) 
yellow = (255, 255, 0)
blue = (0, 0, 255)   
red = (255, 0, 0)   


boundary_colors = [
    (255, 0, 0), 

]


clock = pygame.time.Clock()


snake_size = 20
base_snake_speed = 10
snake_speed = base_snake_speed


score = 0
font = pygame.font.SysFont(None, 34) 
game_over_font = pygame.font.SysFont(None, 60) 


def show_score():
    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, [0, 0])  


def show_game_over():
    game_over_text = game_over_font.render("Game Over", True, black)
    screen.blit(game_over_text, [window_size[0] // 2 - 100, window_size[1] // 3])

def draw_button(text, x, y, width, height):
    pygame.draw.rect(screen, blue, [x, y, width, height])
    button_text = font.render(text, True, white)
    screen.blit(button_text, [x + 0, y + 15])


def draw_boundary():
   
    thickness = 5 
    for i in range(len(boundary_colors)):
        pygame.draw.rect(screen, boundary_colors[i], 
                         [i * thickness, i * thickness, window_size[0] - i * 2 * thickness, window_size[1] - i * 2 * thickness], thickness)


def game_loop():
    global score, snake_speed


    snake_x = window_size[0] // 2 
    snake_y = window_size[1] // 2
    dx = 0
    dy = 0
    snake_body = []
    snake_length = 1
    score = 0

    food_size = 20
    food_x = random.randrange(0, window_size[0] - food_size, food_size)
    food_y = random.randrange(0, window_size[1] - food_size, food_size)

    running = True
    game_over = False


    while running:
        while game_over:
            screen.fill(white)
            show_game_over()
            draw_button("Play Again", window_size[0] // 2 - 60, window_size[1] // 2, 120, 50)
            pygame.display.update()

      
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    
                    if window_size[0] // 2 - 60 <= mouse_x <= window_size[0] // 2 + 60 and window_size[1] // 2 <= mouse_y <= window_size[1] // 2 + 50:
                        game_loop() 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -snake_speed
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = snake_speed
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -snake_speed
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = snake_speed

       
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            snake_speed = base_snake_speed * 2 
        else:
            snake_speed = base_snake_speed  

      
        snake_x += dx
        snake_y += dy

       
        if snake_x < 5 or snake_x >= window_size[0] - 5 or snake_y < 5 or snake_y >= window_size[1] - 5:
            game_over = True  

      
        if snake_x == food_x and snake_y == food_y:
            food_x = random.randrange(0, window_size[0] - food_size, food_size)
            food_y = random.randrange(0, window_size[1] - food_size, food_size)
            snake_length += 1  
            score += 2 

        
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0] 

        for segment in snake_body[:-1]: 
            if snake_head == segment:
                game_over = True

      
        screen.fill(white)

        draw_boundary()


        for segment in snake_body:
            pygame.draw.rect(screen, green, [segment[0], segment[1], snake_size, snake_size])

     
        pygame.draw.rect(screen, green, [food_x, food_y, food_size, food_size])

  
        show_score()

   
        pygame.display.update()


        clock.tick(10)


game_loop()


pygame.quit()
sys.exit()
