class Environment:
    
    r_earth = 6.371*10**6
    g_mean = 9.80665
    
    def __init__(self, wind=0, base_alt=0):
        self.wind = wind
        self.base_alt = base_alt
    
    def get_wind():
        return wind
    
    
    # https://www.grc.nasa.gov/WWW/K-12/airplane/atmosmet.html
    def temp_dens(self, alt):
        if alt < 36152:
            temp = 15.04 - 0.00649 * alt
            dens = 101.29 * ((temp + 273.1)/288.08)**5.256
        else if alt < 25000:
            temp = -56.46
            dens = 22.65 * e^(1.73 - 0.000157*h=alt)
        else:
            temp = -131.21 + 0.00299*alt
            dens = 2.488 * ((temp+273.1)/216.6)**-11.388
        return temp, dens
    def get_density(self, alt):
        temp, dens = temp_dens(alt)
        return dens
    def get_temp(self, alt):
        temp, dens = temp_dens(alt)
        return temp
    
    def get_gravity_acel(self, alt):
        return g_mean * (r_earth / (r_earth + alt + base_alt))**2