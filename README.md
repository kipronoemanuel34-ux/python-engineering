# Python for Mechanical Engineering

Small programs I wrote while learning Python, using real engineering
calculations. I also check my results against 3D models I make in
Autodesk Fusion.

## Programs
- engineering1.py: Celsius to Fahrenheit converter
- engineering2.py: stress calculator (force / area) with a safe/unsafe check
- engineering4.py: rod stress check for steel, aluminium and copper,
  using a safety factor
- engineering5.py: the same check, repeatable for many parts in one run
- engineering6.py: stress check for a rod with a hole through it
  (area = outer circle minus hole), with input checks

## What I learned
- Stress = force / area, and allowable stress = yield strength / safety factor
- A hole reduces the load-carrying area, so the same force gives a
  higher stress
- Checking my code against a CAD model: the rod's area and mass from
  Fusion matched my hand calculations

## Limitations
These are learning examples, not design tools. Real design checks many
more things, and the material values are rough teaching numbers.

## Tools used
Python, Autodesk Fusion

## Author
EMANUEL
