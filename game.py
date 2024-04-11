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

run = True
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False

    window.blit(bg,(0,0))


 
    display.update()
    fps.tick(60)