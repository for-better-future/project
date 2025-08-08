import numpy as np

def on_earth(c):
 t=float(input("enter the years spend on spaceship: \n"))
 c=299792458
 t_dash=float(0)
 '''t_dash is time spend on earth'''
 v=int(input("enter the velocity of spaceship: \n"))
 denom=(np.sqrt(1-((v*v)/(c*c))))
 t_dash=(t)/denom
 print(t_dash)

def on_spaceship(c):
 t_dash=float(input("enter the years spend on earth: \n"))
 c=299792458
 t=float(0)
 v=int(input("enter the velocity of spaceship: \n"))
 denom=(np.sqrt(1-((v*v)/(c*c))))
 t=t_dash*denom
 print(t)

def cnot_earth(c):
 t=float(input("enter the years spend on spaceship: \n"))
 c=float(input("enter speed of light: \n"))
 t_dash=float(0)
 '''t_dash is time spend on earth'''
 v=int(input("enter the velocity of spaceship: \n"))
 denom=(np.sqrt(1-((v*v)/(c*c))))
 t_dash=(t)/denom
 print(t_dash)

def on_spaceship(c):
 t_dash=float(input("enter the years spend on earth: \n"))
 c=float(input("enter speed of light: \n"))
 t=float(0)
 v=int(input("enter the velocity of spaceship: \n"))
 denom=(np.sqrt(1-((v*v)/(c*c))))
 t=t_dash*denom
 print(t)

