import pygame as pg 
import numpy as np
import math
from pygame import mixer
pg.init()

#screen/window
width ,height =800 ,600
screen=pg.display.set_mode((width,height))

#title of the game
pg.display.set_caption("Time Dilation Visualization")

#background
background=pg.image.load(("milky-way-full-stars-space.jpg"))

#background sound
mixer.music.load("WhatsApp Audio 2025-07-23 at 00.36.22_04af482e.wav")
mixer.music.play(-1)
#icon
icon=pg.image.load(("clock.png"))
pg.display.set_icon(icon)


#text 
t_dash=float(0)
font=pg.font.Font("freesansbold.ttf",24)
textx=10
texty=10
def show_year_on_earth(x,y):
    year_earth=font.render("YEAR's ON EARTH: " + str(t_dash),True,(255,255,255))
    screen.blit(year_earth,(textx,texty))


t=float(0)
fonts=pg.font.Font("freesansbold.ttf",24)
textsx=10
textsy=40
def show_year_on_spaceship(x,y):
    year_spaceship=font.render("YEAR's ON SPACESHIP: " + str(t),True,(255,255,255))
    screen.blit(year_spaceship,(textsx,textsy))





#earth
earthimg=pg.image.load(("earth-icon.png"))
earthx=250
earthy=275
earthchange=0
earthstate=True
#spaceship
spaceshipimg=pg.image.load(("space-ship-icon.png"))
spaceshipx=320
spaceshipy=284
spaceshipchangex=0
spaceshipchangey=0
spaceshipstate=True
# collision 
collisionimg=pg.image.load(("collision.png"))
collisionx=250
collisiony=275
collisionstate=False

def spaceship(x,y):
  if spaceshipstate is True:
     screen.blit(spaceshipimg,(x,y))


def earth(x,y):
  if earthstate is True:
     screen.blit(earthimg,(x,y))

def iscollision(earthx,earthy,spaceshipx,spaceshipy):
    diff=np.sqrt((math.pow((earthx-spaceshipx),2)+(math.pow((earthy-spaceshipy),2))))
    if diff < 62:
        global collisionstate
        collisionstate=True
        collisionx=earthx
        collisiony=(earthy)-20
        screen.blit(collisionimg,(collisionx,collisiony))
        return True
    else:
        return False


def on_spaceship():
 global t_dash
 global t
 c=299792458
 t=float(0)
 v=200000000#int(input("enter the velocity of spaceship: \n"))
 denom=(np.sqrt(1-((v*v)/(c*c))))
 t=t_dash*denom

 





#add collision sound 
#add propulsion sound
#add proper setup for display
#finally make it neat and clean














#game loop
running=True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT :
            running=False
        
        
        if event.type == pg.KEYDOWN :
                 if event.key == pg.K_RIGHT:
                     spaceshipchangex += 0.3
                     earthchange -=0.3
                     t_dash+=1
                     propultion_sound=mixer.Sound("propultion.wav")
                     propultion_sound.play()
                 if event.key == pg.K_LEFT:
                     spaceshipchangex =- 0.3
                     earthchange +=0.3
                     t_dash-=1

                 if event.key == pg.K_UP:
                     spaceshipchangey -= 0.3
                     t_dash+=0.5
  
                 if event.key == pg.K_DOWN:
                     spaceshipchangey += 0.3
  
        if event.type == pg.KEYUP :
                 if event.key == pg.K_RIGHT or event.key == pg.K_LEFT or event.key == pg.K_UP or event.key == pg.K_DOWN :
                     earthchange=0
                     spaceshipchangex=0
                     spaceshipchangey=0
                     
    
    on_spaceship()
    show_year_on_earth(textx,texty)
    show_year_on_spaceship(textsx,textsy)

    #collision
    collision=iscollision(earthx,earthy,spaceshipx,spaceshipy)
    if collision:
        earthstate=False
        spaceshipstate=False
        collision_sound=mixer.Sound("collision.wav")
        collision_sound.play()
    
    
    else:
      earthx += earthchange
    
      spaceshipx += spaceshipchangex
      if spaceshipx >= 800:
          spaceshipx=0
      elif spaceshipx <= 0:
          spaceshipx=800
    
      spaceshipy += spaceshipchangey
      if spaceshipy >= 600:
          spaceshipy=0
      elif spaceshipy <= 0:
          spaceshipy=600



    iscollision(earthx,earthy,spaceshipx,spaceshipy)
    earth(earthx,earthy)
    spaceship(spaceshipx,spaceshipy)
    iscollision(earthx,earthy,spaceshipx,spaceshipy)
    pg.display.update()

        