import energy_transmission as engt 

energy= 5e6
dt=1

for i in range(10):
    energy, received = engt.transmit_energy(energy, dt)
    print(f"t={i+1}s | stored={energy/1e6:.2f} MJ | sent={received/1e6:.2f} MJ")