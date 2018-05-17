import pygame
from Communication.tcp import Client

server = Client('192.168.42.71',1234)

grid_size = 10

x=50
y=50

if server.connected == False:
    print('Nepodarilo se pripojit.')
else:

    pygame.init()

    screen = pygame.display.set_mode((800,800))
    pygame.time.set_timer(pygame.USEREVENT + 1,1)
    
    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_END):
            server.close()
            break
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_w]:
                server.write('w')
            elif pygame.key.get_pressed()[pygame.K_a]:
                server.write('a')
            elif pygame.key.get_pressed()[pygame.K_s]:
                server.write('s')
            elif pygame.key.get_pressed()[pygame.K_d]:
                server.write('d')
        if event.type == (pygame.USEREVENT + 1):
            i = server.read(1)
            print(i)
            if i == '\n':
                x=0
                y+=grid_size
                i = server.read(1)                
            if i == '!':
                x=0
                y=0
                break
            elif i == '#':
                pygame.draw.rect(screen, (0,0,255),(x,y,grid_size,grid_size))
                x+=grid_size
                i = server.read(1)
                pygame.display.flip()
            elif i == '*':
                pygame.draw.circle(screen, (255,0,0),(x,y),grid_size // 2)
                x+=grid_size
                i = server.read(1)
            elif i == '':
                x+=grid_size
                i = server.read(1)
            elif i == 'a':
                pygame.draw.circle(screen, (255,255,0),(x,y),grid_size // 2)
                x+=grid_size
                i = server.read(1)
            elif i == 'b':
                pygame.draw.circle(screen, (0,255,0),(x,y),grid_size // 2)
                x+=grid_size
                i = server.read(1)
            elif i == 'c':
                pygame.draw.circle(screen, (255,255,255),(x,y),grid_size // 2)
                x+=grid_size
                i = server.read(1)







pygame.quit()
