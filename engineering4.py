import math

S = "MPa"
A = "mm^2"

materials = {
    "steel": 250,
    "aluminium": 275,
    "copper": 70
}

def circle_area(d):
    return round(math.pi * d**2 / 4, 2)

def stress(force, area):
    return round(force / area, 2)

def check_status(result, allowable):
    if result < allowable:
        return "safe"
    else:
        return "unsafe"

force = float(input("Enter the force in N:"))
rod_diameter = float(input("Enter the rod diameter in mm:"))
name = input("Enter the material's name:")

if name in materials:
    allowable_stress = materials[name] / 2
    print(f"The allowable stress is : {allowable_stress} {S}")

    area = circle_area(rod_diameter)
    print(f"the area is: {area} {A}")

    result = stress(force, area)
    print(f"the stress is : {result} {S}")

    print(check_status(result, allowable_stress))
else:
    print("Material not found. Choose steel, aluminium or copper")