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

while True:
    answer = input("Type 'no' to quit, anything else to continue: ").lower()
   
    if answer == "no":
        break

    force = float(input("Enter the force in N:"))
    rod_diameter = float(input("Enter the rod diameter in mm:"))
    name = input("Enter the material's name:")
    hole_diameter = float(input("Enter the hole diameter:"))
    if hole_diameter >= rod_diameter:
         print("The hole diameter must be less than the rod diameter.")
    else:
      if name in materials:
         allowable_stress = materials[name] / 2
         print(f"The allowable stress is : {allowable_stress} {S}")

         area = circle_area(rod_diameter) - circle_area(hole_diameter)
         print(f"the area is: {area} {A}")

         result = stress(force, area)
         print(f"the stress is : {result} {S}")

         print(check_status(result, allowable_stress))
      else:
         print("Material not found. Choose steel, aluminium or copper")
print("Goodbye")