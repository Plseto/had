import pygame
import random

pygame.init()

window_s = 800
window_v = 800
grid_size = 20
tail = []
new_tail = []
enemy = [[random.randrange( 10 , window_s-10,grid_size) - grid_size // 2,random.randrange( 10 , window_s-10,grid_size) - grid_size // 2]]

screen = pygame.display.set_mode((window_s,window_v))

me_x = random.randrange( 10 , window_s-10,grid_size)
me_y = random.randrange( 10 , window_v-10,grid_size)

food_x = random.randrange( 10 , window_s-10,grid_size)
food_y = random.randrange( 10 , window_v-10,grid_size)

new_me_x = 0
new_me_y =0

smer = -1

pygame.draw.circle(screen, (0,255,0),(food_x,food_y),grid_size // 2)
pygame.draw.circle(screen, (255,255,255),(me_x,me_y),grid_size // 2)
pygame.display.flip()

pygame.time.set_timer(pygame.USEREVENT + 1,250)

while True:
    event = pygame.event.poll()
    if event.type == (pygame.USEREVENT + 1):
        me_x += new_me_x
        me_y += new_me_y
        new_tail.append([me_x, me_y])
        n = 0
        for i in range(0,len(tail)-1):
            new_tail.append(tail[n])
            n += 1  
        tail = new_tail
        new_tail = []
        screen.fill((0,0,0))
        pygame.draw.circle(screen, (0,255,0),(food_x,food_y),grid_size // 2)
        m = 0
        for i in range(len(tail)):
            pygame.draw.circle(screen, (255,255,255),(tail[m][0],tail[m][1]),grid_size // 2)
            m += 1
        m = 0
        for i in range(len(enemy)):
            pygame.draw.rect(screen, (255,0,0),(enemy[m][0],enemy[m][1],grid_size,grid_size))
            m += 1
        pygame.display.flip()
        print(tail)
        print(enemy)
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_END):
        break
    if me_x <= 0 or me_y <= 0 or me_x >= window_s or me_y >= window_v:
        break
    if event.type == pygame.KEYDOWN:
        pygame.key.get_pressed()
        if pygame.key.get_pressed()[pygame.K_w] and smer != 2:            
            new_me_x = 0
            new_me_y = 0
            new_me_y = -grid_size
            smer = 0
        elif pygame.key.get_pressed()[pygame.K_a] and smer != 3:            
            new_me_x = 0
            new_me_y = 0
            new_me_x = -grid_size
            smer = 1
        elif pygame.key.get_pressed()[pygame.K_s] and smer != 0:
            new_me_x = 0
            new_me_y = 0
            new_me_y = grid_size
            smer = 2
        elif pygame.key.get_pressed()[pygame.K_d] and smer != 1:            
            new_me_x = 0
            new_me_y = 0
            new_me_x = grid_size
            smer = 3
    if me_x == food_x and me_y == food_y:        
        tail.append([me_x, me_y])
        food_x = random.randrange( 10 , window_s-10,grid_size)
        food_y = random.randrange( 10 , window_v-10,grid_size)
        enemy.append([random.randrange( 10 , window_s-10,grid_size) - grid_size // 2,random.randrange( 10 , window_s-10,grid_size) - grid_size // 2])
    m = 0
    for g in range(len(enemy)):
        if me_x == enemy[m][0] + grid_size // 2 and me_y == enemy[m][1] + grid_size // 2:
            break
        m += 1











pygame.quit()
