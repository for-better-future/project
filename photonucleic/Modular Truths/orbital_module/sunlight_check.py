import numpy as np
import math
import _constants as ct
import orbital as obt

P = obt.satellite_pos(ct.R + 500e3,1000)
sun_dist = 1e11
S = np.array([-sun_dist,0])
E = np.array([0,0])
R = ct.R

def is_litt(S,P,E,R):

 # first calculate direction of rays

 d = P-S

 #calculate vector from earth to sun
 #this tells us where earth is relative to the ray's start.
 f = S-E

 #find closest pt. on ray from earth which is perpendicular distance

 t = - np.dot(f,d) / np.dot(d,d)  #this gives us the closest point

 #if t==0 then we are at sun and t==1 we are at satellite
 #0<t>1 somewhere in between both

 #check if earth is between sun and satellite
 if t<0 :     #for this condition sunlight is always there
    return True

 #now lets check for if earth is in between
 #check the cloest pt

 closest = S+t*d
 distance = np.linalg.norm(closest-E) 
 
 #this gives us the distance from earth center to closest pt.
 #why we used linalg.norm because we needed one sigle value it converts vector value into one 
 #single value                                   

 if distance>R:
   return True
 else:
   return False