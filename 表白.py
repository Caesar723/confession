import pygame
import random
def showMessage(text,size,colour,p):
    fon=pygame.font.Font(None,size)
    sur=fon.render(text,True,colour)
    screen.blit(sur,p)
pygame.init()
screen=pygame.display.set_mode([300,300])
running=True
nox=190
noy=250
yesx=60
yesy=250
get=False
text="Do you love me?"
clock=pygame.time.Clock()
counter=0
while running:
    screen.fill([10,0,30])
    c = pygame.mouse.get_pos()
    img = pygame.image.load("IMG_0199.JPG")
    bodysize = pygame.transform.scale(img, (180, 180))
    bodyxy = bodysize.get_rect(center=(140, 150))
    screen.blit(bodysize, bodyxy)
    for event in pygame.event.get():
        if c[0] > yesx - 20 and c[0] < yesx + 20 and c[1] < yesy + 20 and c[1] > yesy - 20 and event.type ==pygame.MOUSEBUTTONDOWN:
            text ="I love you too"
            get=True
        if c[0] > nox - 20 and c[0] < nox + 20 and c[1] < noy + 20 and c[1] > noy - 20:
            nox = random.randint(0, 250)
            noy = random.randint(0, 250)
    showMessage(text,20,[255,255,255],[90,30])
    showMessage("Yes", 20, [255, 255, 255], [yesx,yesy])
    showMessage("No", 20, [255, 255, 255], [nox, noy])
    if get==True:
        counter+=1
        if counter==180:
            running=False
    clock.tick(60)
    pygame.display.flip()
pygame.quit()