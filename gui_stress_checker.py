import tkinter as tk
import math 

materials = {"steel": 250, "aluminium": 275, "copper": 70}

def check():
    try:
        d = float(diameter_entry.get())
        force =float(force_entry.get())
        holed = float(holed_entry.get())
    except ValueError:
        result_label.config(text="Enter a number")
        return 
    if d <= 0 or force <= 0 or holed < 0:
        result_label.config(text="Rod and force must be above zero. \nHole can't be negative.")
        return
    if holed >= d :
        result_label.config(text="The hole diameter must be less than the rod diameter.")
        return
    name = material_var.get()
    allowable_stress = materials[name] / 2
        
    area = math.pi * d**2 / 4 - math.pi * holed**2 / 4
    stress = force / area
    if stress < allowable_stress:
        verdict = "safe"
    else:
        verdict = "unsafe"
    
    result_label.config(text=f"Area: {area:.2f} mm^2\nStress: {stress:.2f} MPa\nAllowable stress: {allowable_stress:.2f} MPa\n{verdict}")


window = tk.Tk()
window.title("Stress Checker")

material_var = tk.StringVar(value="steel")

tk.Label(window, text="Diameter (mm):").pack()
diameter_entry = tk.Entry(window)
diameter_entry.pack()

tk.Label(window, text="Force (N):").pack()
force_entry = tk.Entry(window)
force_entry.pack()

tk.Label(window, text="Diameter of the hole (mm):").pack()
holed_entry = tk.Entry(window)
holed_entry.pack()

tk.Label(window, text="Material:").pack()
tk.OptionMenu(window, material_var, *materials.keys()).pack()

tk.Button(window, text="Check", command=check).pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()