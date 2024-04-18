from pygame import *

widht=900
hight=500

window = display.set_mode((widht, hight))
fps = time.Clock()
bg = transform.scale(image.load('bg.jpg'),(widht,hight))
class Rocket():
    def __init__(self,img, x, y, widht_rocket, hight_rocket, speed):
        self.image = transform.scale(image.load(img),(widht_rocket, hight_rocket))
        self.image_hit = self.image.get_rect()
        self.image_hit.x = x
        self.image_hit.y = y
        self.speed = speed
    def show_s(self):
        window.blit(self.image,(self.image_hit.x, self.image_hit.y))

class Rocket_player(Rocket):
    def updete_r(self):
        keys = key.get_pressed()
        if keys[K_w] and self.image_hit.y >5:
            self.image_hit.y -= self.speed
        if keys[K_s] and self.image_hit.y < widht -80:
            self.image_hit.y += self.speed

class Player_rocket(Rocket):
    def updete_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.image_hit.y >5:
            self.image_hit.y -= self.speed
        if keys[K_DOWN] and self.image_hit.y < widht -80:
            self.image_hit.y += self.speed
            
        
pl1 = Rocket_player("player.png",10,250,25,100,5)
pl2 = Player_rocket("player.png",860,250,25,100,5)
ball = Rocket('ball.png',200, 200, 35, 35, 4)
run = True
speed_x = 3
speed_y = 3


while run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    window.blit(bg,(0,0))
    pl1.show_s()
    pl1.updete_r()
    pl2.show_s()
    pl2.updete_r()
    ball.show_s()

    ball.image_hit.x += speed_x
    ball.image_hit.y += speed_y

    if sprite.collide_rect(pl1, ball) or sprite.collide_rect(pl2, ball) :
        speed_x *= -1
        speed_y *= 1

    if ball.image_hit.y < 10:
        speed_y *= 1
    if bal.image_hit.x > 470:
        speed_x *= 1


 
    display.update()
    fps.tick(60)
