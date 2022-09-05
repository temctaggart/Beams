# Beam Selection Steps

1. Calculate Z (use maximum stress equation, solve for Z).
2. Use calculated value of Z to look up the material size.
3. Record I for that beam.
4. Calculate I (use maximum deflection equation, solve for I).
5. Use calculated value of I to look up the material size.
6. Record Z for that beam.
7. Choose the beam that has an acceptable Z for strength and I for deflection.
8. Re-calculate using the value of I and Z for the chosen material."

## main.py
  - class size_beam:
    - class attributes
      - fs - factor of safety
      - yield_strength = Yield Strength of Material (psi)
      - mod_e - Modulus of Elasticity (psi)
    - object attributes
      - load - Uniform Load (lbs)
      - length - Length of beam (in)
      - x - arbitrary distance from the end of the beam (in)
      - stress_allow = stress_max/FS (psi)
      - deflection_max = maximum deflection allowed for this beam (in)
      - z - Section Modulus (in^3)
      - i - Moment of Inertia (in^4)
    - methods
      - calculate z
      - lookup material for z
        - record i
      - calculate i
      - lookup material for i
        - record z
      - lookup material that matches z and i requirements
        - print list of acceptable material
      - Choose material from list
        - calculate stress and deflection using chosen material (z and i)
## Calculations
Create a module for each end condition and load type
