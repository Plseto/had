import pygame

pygame.init()

grid = 20
window_s = 800
window_v = 800
start = (40, 40)
x = 60
y = 60

green = pygame.Color('green')
blue = pygame.Color('blue')

pygame.init()

scr = pygame.display.set_mode((window_s,window_v))

class had:
    def __init__ (self,start,smer = -1,color = green,key = (pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d)):
        self.tail = [start]
        self.key = key
        self.color = color
        self.smer = smer

    def move(self,key):
        if key == self.key[0] and self.smer != 2:
            self.smer = 0
            y -= 1
        elif key == self.key[1] and self.smer != 4:
            self.smer = 1
            x -= 1
        elif key == self.key[2] and self.smer != 0:
            self.smer = 2
            y = 1
        elif key == self.key[3] and self.smer != 1:
            self.smer = 3
            x = 1
        coor = (x, y)
        if coor in self.tail:
            return False
        self.last = self.tail[-1]
        for i in range(len(self.tail) - 1, 0, -1):
            self.tail[i] = self.tail[i-1]
        self.tail[0] = coor
        return True
        
    def check_apple(self, apple):
        if self.tail[0] == apple:
            self.tail.append(self.tail)
            return True
        return False

    def draw(self, surface):
        for coor in self.tail:
            c = (pos[0] * raster, pos[1] * raster)
            pygame.draw.circle(scr, self.color, pygame.circle(c, (grid // 2)))

start = [(x + 1, y) for x in range(2)]

key = ((pygame.K_w,pygame.K_a,pygame.K_s,pygame.K_d),
       (pygame.K_UP,pygame.K_LEFT,pygame.K_DOWN,pygame.K_RIGHT))
color = ((pygame.Color('green')),(pygame.Color('blue')))

snake = [had(start[i], color = color[i], key = key[i]) for i in range(2)]














