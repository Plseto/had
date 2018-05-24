import pygame
from Communication.tcp import Client

##'192.168.42.102',11111
##'192.168.42.71',1234

server = Client('192.168.42.71',1234)

grid_size = 10

mapa = []
x=0
y=0

if server.connected == False:
    print('Nepodarilo se pripojit.')
else:

    pygame.init()

    screen = pygame.display.set_mode((800,800))
    
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
##        while server.read(1) != '!':
##            mapa.append(server.read(1))
##        else:
##            mapa.append(server.read(1))
##            break
##        for i in mapa:
##            if i == '\n':
##                x=0
##                y+=grid_size                
##            elif i == '!':
##                x=0
##                y=0
##                break
##            elif i == '#':
##                pygame.draw.rect(screen, (0,0,255),(x,y,grid_size,grid_size))
##                x+=grid_size
##                pygame.display.flip()
##            elif i == '*':
##                pygame.draw.circle(screen, (255,0,0),(x,y),grid_size // 2)
##                x+=grid_size
##            elif i == '':
##                x+=grid_size
##            elif i == 'a':
##                pygame.draw.circle(screen, (255,255,0),(x,y),grid_size // 2)
##                x+=grid_size
##            elif i == 'b':
##                pygame.draw.circle(screen, (0,255,0),(x,y),grid_size // 2)
##                x+=grid_size
##            elif i == 'c':
##                pygame.draw.circle(screen, (255,255,255),(x,y),grid_size // 2)
##                x+=grid_size



pygame.quit()
