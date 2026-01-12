import numpy as np


MAX_TX_power = 2e5
TX_eff = 0.6

def transmit_energy(energy_stored,dt):
    if energy_stored <=0:
        return energy_stored, 0.0
    
    E_possible = MAX_TX_power * dt
    E_sent = min(energy_stored,E_possible)
    
    energy_stored -= E_sent

    E_received = E_sent*TX_eff

    return energy_stored, E_received