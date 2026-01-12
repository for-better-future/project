import sunlight_check as schk
import orbital as obt
import numpy as  np
import math
import _constants as ct


R = ct.R 
r= R+200e3
MU = ct.GM
omega = math.sqrt(MU / r**3)
T = 2*math.pi/omega
t = T/2 

P = np.array(obt.satellite_pos(r,t))
sun_dist = 1e11
S = np.array([-sun_dist,0])
E = np.array([0,0])

print("x =", P[0])
check = schk.is_litt(S,P,E,R)

print(check)