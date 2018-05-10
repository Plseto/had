import pygame
from Communication.tcp import Client

server = Client('192.168.42.69',1234)

grid_size = 10

x=0
y=0

if server.connected == False:
    print('Nepodarilo se pripojit.')
else:

    pygame.init()

    screen = pygame.display.set_mode((200,200))

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_END):
            server.close()
            break
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_w]:
                server.write('w')
                print('nahoru')
            elif pygame.key.get_pressed()[pygame.K_a]:
                server.write('a')
                print('doleva')
            elif pygame.key.get_pressed()[pygame.K_s]:
                server.write('s')
                print('dolu')
            elif pygame.key.get_pressed()[pygame.K_d]:
                server.write('d')
                print('d')
        while True:
            i = server.read(1)
            if i == '\n':
                x=0
                y+=1
            elif i == '!':
                x=0
                y=0
                break
            elif i == '#':
                pygame.draw.rect(screen, (0,0,255),(x,y,grid_size,grid_size))
                x+=grid_size
            elif i == '*':
                pygame.draw.circle(screen, (255,0,0),(x,y),grid_size // 2)
                x+=grid_size
            elif i == '':
                None
                x+=grid_size
            elif i == 'a':
                pygame.draw.circle(screen, (255,255,0),(x,y),grid_size // 2)
                x+=grid_size
            elif i == 'b':
                pygame.draw.circle(screen, (0,255,0),(x,y),grid_size // 2)
                x+=grid_size
            elif i == 'c':
                pygame.draw.circle(screen, (255,255,255),(x,y),grid_size // 2)
                x+=grid_size
            







pygame.quit()
