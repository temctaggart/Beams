"""
Description: Calculations for various support and load conditions

Calculations based on formulas from Machinery's Handbook 25

  Calculate:
    Stress at any point
    Stress at critical points
    Deflection at any point
    Deflection at critical points

Variable Definitions:
    fs - Factor of Safety
    load - Uniform Load (lbs)
    length - Length of beam (in)
    x - arbitrary distance from the end of the beam (in)
    yield_strength = Yield Strength of Material (psi)
    stress_allow = stress_max/FS (psi)
    deflection_max = maximum deflection allowed for this beam (in)
    mod_e - Modulus of Elasticity (psi)
    z - Section Modulus (in^3)
    i - Moment of Inertia (in^4)
"""
import calculations


class Beam:
    # Class Attributes/Variables

    # Class Constructor/Initializer
    def __init__(self, load, length, deflection_max, fs=1.5, yield_strength=55000, modulus_of_elasticity=29E6):
        self.load = load
        self.length = length
        self.deflection_max = deflection_max
        self.fs = fs
        self.yield_strength = yield_strength
        self.modulus_of_elasticity = modulus_of_elasticity

    def find_z(self):
        a = calculations.z_ff_ul
        bz = a(self.load, self.length, self.yield_strength, self.fs)
        return bz

    def find_i(self):
        bi = calculations.i_ff_ul(self.load, self.length, self.modulus_of_elasticity, self.deflection_max)
        return bi

    def find_beam(self):
        # Use this method to lookup beams from xml data.
        pass


# Methods
'''
        z_mod = (self.load*self.length)/(12 * (self.yield_strength/self.fs))
        return z_mod

    def i_ff_ul(self):
        mom_inertia = (self.load*(self.length**3))/(384*self.modulus_of_elasticity*self.deflection_max)
        return mom_inertia



def find_beam():
    print('hello')
    beam1 = Beam(10000, 180, 0.3125)
    b1z = calculations.z_ff_ul(beam1.load, beam1.length, beam1.yield_strength, beam1.fs)
    b1i = calculations.i_ff_ul(beam1.load, beam1.length, beam1.modulus_of_elasticity, beam1.deflection_max)

    print('Z = {:.4f}'.format(b1z))
    print('I = {:.4f}'.format(b1i))
'''


def main():
    # print('This module is not intended to be used as a script.')
    beam1 = Beam(10000, 120, 0.3125)
    print('Z = {:.4f}'.format(beam1.find_z()))
    print('I = {:.4f}'.format(beam1.find_i()))


if __name__ == '__main__':
    main()
