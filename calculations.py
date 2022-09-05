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

Method names
    z_ff_ul - find section modulus, fixed at both ends, uniform load
    i_ff_ul - find moment of inertia, fixed at both ends, uniform load
    z_ss_ul - find section modulus, simply supported at both ends, uniform load
    i_ss_ul - find moment of inertia, simply supported at both ends, uniform load
"""
# Methods to find Z and I


def z_ff_ul(load, length, yield_strength, fs):
    z_mod = (load*length)/(12 * (yield_strength/fs))
    return z_mod


def i_ff_ul(load, length, modulus_of_elasticity, deflection_max):
    mom_inertia = (load*(length**3))/(384*modulus_of_elasticity*deflection_max)
    return mom_inertia


def z_ss_ul():
    pass


def i_ss_ul():
    pass


def main():
    print('This module is not intended to be used as a script.')


if __name__ == '__main__':
    main()
