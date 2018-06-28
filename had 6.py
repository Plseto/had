import pygame
from Communication.tcp import Client

##'192.168.42.102',11111
##'192.168.42.71',1234

##i = server.read(1)

##soubor = open('snake1.txt')
##i=soubor.read()
##soubor.close()

server = Client('localhost',12345)

grid_size = 10

mapa = []
x = 0
y = 0
frame = 0

if server.connected == False:
    print('Nepodarilo se pripojit.')
else:
    server.timeout = 0
    pygame.init()

    screen = pygame.display.set_mode((800,800))

    pygame.time.set_timer(pygame.USEREVENT + 1,100)


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
            while True:
                i = server.read()
                if not i:
                    break
                if i == b'\n':
                    x=0
                    y+=grid_size
                elif i == b'!':
                    x=0
                    y=0
                    pygame.display.flip()
                    screen.fill((0,0,0))
                elif i == b'#':
                    pygame.draw.rect(screen, (0,0,255),(x,y,grid_size,grid_size))
                    x+=grid_size
                elif i == b'*':
                    pygame.draw.circle(screen, (255,0,0),(x+grid_size // 2,y+grid_size // 2),grid_size // 2)
                    x+=grid_size
                elif i == b' ':
                    x+=grid_size
                elif i == b'a':
                    pygame.draw.circle(screen, (255,255,0),(x+grid_size // 2,y+grid_size // 2),grid_size // 2)
                    x+=grid_size
                elif i == b'b':
                    pygame.draw.circle(screen, (0,255,0),(x,y),grid_size // 2)
                    x+=grid_size
                elif i == b'c':
                    pygame.draw.circle(screen, (255,255,255),(x,y),grid_size // 2)
                    x+=grid_size

pygame.quit()
