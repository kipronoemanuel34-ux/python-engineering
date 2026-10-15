S = "MPa"
area = float(input("Enter the area in mm^2:"))
force = float(input("Enter the force in N:"))

def stress(force, area):
    stress = force/area
    return stress
print(f"The stress is: {stress(force, area)} {S}")
result = stress(force, area)
def check_status(result):
  if result < 250:
     return "Safe"
  else:
     return "Unsafe; exceeds yield strength"
print(check_status(result))
  