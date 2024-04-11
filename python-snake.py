#snake game
import pygame
import time
import random

pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
pink=(213,50,80)
blue=(50,153,213)
yellow=(255,255,102)
green=(0,255,0)

dis_width=800
dis_height=600
snake_block=10
snake_speed=30

clock=pygame.time.Clock()
font_style=pygame.font.SysFont("bahnschrift",35)
font_style_s=pygame.font.SysFont("bahnschrift",25)
score_font=pygame.font.SysFont("comicsansms",35)
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Snake game')

def message(msg, color):
    mesg=font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/3.3, dis_height/2])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def Your_score(exp, needed_exp):
    value = font_style_s.render("Exp: " + str(exp) + "/" + str(needed_exp), True, pink)
    dis.blit(value, [22,22])

def gameLoop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_List = []
    Length_of_snake=1

    exp=0
    needed_exp=2

    foodx=round(random.randrange(0, dis_width - snake_block)/10.0)*10.0
    foody=round(random.randrange(0, dis_width - snake_block)/10.0)*10.0

    while not game_over:
        while game_close==True:
            dis.fill(black)
            message("Q-Quit or R-Restart", pink)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True

        x1+=x1_change
        y1+=y1_change
        dis.fill(black)
        controls=font_style_s.render("Controls: W,A,S,D", True, pink)
        dis.blit(controls, [590,22])
        
        pygame.draw.rect(dis, pink, [foodx, foody, snake_block, snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]
        
        our_snake(snake_block, snake_List)
        Your_score(exp, needed_exp)
        pygame.display.update()

        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            exp+=1
            if exp==needed_exp:
                Length_of_snake+=1
                needed_exp+=2
                exp=0
            print(exp, needed_exp)
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()

gameLoop()