import orbital
r = int(6.371e6 + 2e6)
t = 2e100
import math

result=orbital.satellite_pos(r,t)
print(result)
