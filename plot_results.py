import pandas as pd
import matplotlib.pyplot as plt

columns = ["force", "rod_diameter", "hole_diameter", "material", "stress", "status"]
materials = {"steel": 250, "aluminium": 275, "copper": 70}
data = pd.read_csv("results.csv", header=None, names=columns)
data["allowable"] = data["material"].map(materials) / 2
print(data)

data["label"] = data["material"] + " " + data["force"].astype(int).astype(str) + " N"

colors = []
for s in data["status"]:
    if s == "safe":
        colors.append("green")
    else:
        colors.append("red")

positions = range(len(data))
plt.bar(positions, data["stress"], color=colors)
plt.xticks(positions, data["label"], rotation=30)
plt.ylabel("Stress (MPa)")
plt.title("Stress results from my checks")
plt.tight_layout()
plt.scatter(positions, data["allowable"], marker="_", s=1500, color="black", zorder=3, label="Allowable stress")
plt.legend()
plt.show()
# 84.88MPa is safe for aluminium and steel while unsafe for copper since its allowable stress is below this figure