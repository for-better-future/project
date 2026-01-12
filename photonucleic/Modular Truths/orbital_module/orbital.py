#tells the satellite's position at time
import math
# import constants as cons

'''
this module is used to determine the position of the satellite in space using real
physics formulas.
inputs: radius of the satellite + radius of the earth.
outputs: (X and Y) coordinates of satellite on XY-plane 2D.

'''
GM=3.986e14

def satellite_pos (r ,t):
    #r = radius of the satellite
    #t = how long satellite has been moving in the orbit
    global GM
    MU = GM
    omega= math.sqrt(MU/r**3)
    theta = omega*t

    # X position of the satellite

    X = r*math.cos(theta)

    # Y position of the satellite 

    Y = r*math.sin(theta)

    return(X,Y)
    
    dist= math.sqrt(X**2 + Y**2)
    print(dist)
