import math

S = "MPa"
A = "mm^2"
force = float(input("Enter the force in N:"))
rod_diameter = float(input("Enter the rod diameter in mm:"))

def circle_area(rod_diameter):
        
    area = math.pi * rod_diameter**2 / 4
    return round(area,2)
print(f"The area is:{circle_area(rod_diameter)} {A}")
Area = circle_area(rod_diameter)

def stress(force, Area):
    stress = force / Area
    return round(stress, 2)

print(f"The stress is : {stress(force, Area)} {S}")
result = stress(force, Area)

def check_status(result):
    if result < 250:
        return "safe"
    else:
        return "unsafe"
    
print(check_status(result)) 