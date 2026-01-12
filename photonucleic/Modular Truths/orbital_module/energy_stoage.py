import _constants as ct

def update_energy_storage(
        energy,
        is_sunlit,
        dt,
        panel_area=20.0,
        solar_flux = 1361,
        efficiency=0.30,
        max_capacity=5e9
):
    if is_sunlit:
        power=panel_area*solar_flux*efficiency
        energy += power*dt

    if energy>max_capacity:
        energy=max_capacity

    return energy