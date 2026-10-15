celsius = float(input("Enter temperature in celsius:"))
def celsius_to_fahrenheit(celsius):
    F = (celsius * (9/5) + 32)
    return F
print(f"{celsius} degrees celsius is {celsius_to_fahrenheit(celsius)} degrees fahrenheit")