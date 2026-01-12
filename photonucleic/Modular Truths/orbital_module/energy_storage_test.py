import energy_stoage as engs 
import sunlight_check as schk
import orbital as obt
import _constants as ct
import math
import numpy as np 

# sun_dist = 1e11
# S = np.array([-sun_dist,0])
# E = np.array([0,0])
# R = ct.R
# r= R+200e3
# MU = ct.GM
# omega = math.sqrt(MU / r**3)
# T = 2*math.pi/omega
# t = T/4 
# P = obt.satellite_pos(r,t)





energy = 0.0
dt = 1.0

i = 1
while i > 0:
    energy=engs.update_energy_storage(
        energy=energy
        ,is_sunlit=True 
        ,dt=dt )
    print(f"t={i+1}sec  energy={energy/1e6:.3f} MJ")

# for i in range(5):
#     energy=engs.update_energy_storage(
#         energy=energy
#         ,is_sunlit=False 
#         ,dt=dt )
#     print(f"shadow t={i+1}sec  energy={energy/1e6:.3f} MJ")