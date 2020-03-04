from math import *

#Future reading: https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20010047838.pdf
class Rocket:
    
    def __init__(self, engine, environment, mass=15, diameter=0.1524, cd=1, length=3, cp=0.3,cm=0.35, cm_dry=cm, cm_wet=cm):
        # Rocket state
        self.alt = 0;
        self.dist = 0;
        self.v_alt = 0;
        self.v_dist = 0;
        self.heading = 0;
        
        # Rocket parameters
        self.engine = engine #<Function> engine(time) = thrust
        self.environment = environment #<Environment>
        
        self.mass = mass #in kg
        self.cd = cd
        self.diameter = diameter
        
        self.length = length #in m
        self.cp = cp # center of pressure; 0 to 1: percentage along the rocket
        self.cm_dry = cm # dry center of mass; 0 to 1: percentage along the rocket
        self.cm_wet = cm_wet
        
    
    def f_g(self):
        a_g = self.environment.get_gravity_acel(alt)
        return a_g * self.mass
    
    #https://wright.nasa.gov/airplane/drageq.html
    def f_d(self):
        dens = self.environment.get_density(alt)
        return self.cd * dens * (pi*(self.diameter/2)**2) * (v_alt**2 + v_dist**2) / 2