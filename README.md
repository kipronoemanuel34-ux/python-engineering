# Python for Mechanical Engineering

Small programs I wrote while learning Python, using real mechanical
engineering calculations. Each one builds on the one before, from a
simple unit converter to a stress checker with a window, a database
of results, and a graph. I also checked some of my results against 3D
models I made in Autodesk Fusion (the volume and mass of my modelled
rod matched my hand calculations).

## Programs

| File | What it does |
|---|---|
| `engineering1.py` | Converts Celsius to Fahrenheit using a function |
| `engineering2.py` | Calculates stress (force / area) and compares it with a yield strength of 250 MPa |
| `engineering3.py` | Works out a round rod's area from its diameter, then its stress |
| `engineering4.py` | Adds a materials dictionary (steel, aluminium, copper) and a safety factor of 2 |
| `engineering5.py` | Repeats the check for many parts in one run |
| `engineering6.py` | Handles a rod with a hole through it (area = outer circle minus hole), and rejects a hole that is too big |
| `engineering7.py` | Adds input checking (letters, zero and negative numbers are rejected) and saves every result to `results.csv` |
| `plot_results.py` | Draws a bar graph of the saved results, with each material's allowable stress marked |
| `gui1.py` | A window version of the stress checker, with a material dropdown, a hole diameter box and the same checks |

`results.csv` holds the results saved by `engineering7.py`. Its columns
are: force (N), rod diameter (mm), hole diameter (mm), material,
stress (MPa), and verdict.

## How to run

You need Python 3. Only `plot_results.py` needs extra libraries:

```
pip install pandas matplotlib
```

Then run any program from the folder:

```
python engineering7.py
python plot_results.py
python gui1.py
```

(`tkinter`, used by `gui1.py`, comes with Python.)

## Example

Steel rod, 20 mm diameter, 10 mm hole, 20,000 N:

- Area: 235.62 mm²
- Stress: 84.88 MPa
- Allowable stress: 125 MPa (250 MPa yield strength / safety factor 2)
- Result: **safe**

The same rod in copper has an allowable stress of 35 MPa, so the
same load is **unsafe**. The graph from `plot_results.py` shows this
difference clearly.

## What I learned

- Stress = force / area, and allowable stress = yield strength / safety factor
- A hole reduces the area that carries the load, so the same force
  gives a higher stress
- The order of the steps matters: check the inputs first, then
  calculate, then judge, then show or save the result
- Functions, dictionaries, loops, `try / except`, and reading and
  writing CSV files
- Drawing graphs with pandas and matplotlib
- Building a window with Tkinter

## Limitations

These are learning examples, not design tools. The material values are
rough teaching numbers, and real design checks many more things, such
as fatigue, buckling, stress concentrations and the exact alloy.

## Tools used

Python (pandas, matplotlib, tkinter), Autodesk Fusion, Git and GitHub

## Author

Your Name
