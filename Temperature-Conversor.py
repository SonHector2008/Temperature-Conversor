#Celsius to Fahrenheit: F = (C × 9/5) + 32
#Celsius to Kelvin: K = C + 273.15
#Fahrenheit to Celsius: C = (F - 32) × 5/9
#Fahrenheit to Kelvin: K = (F + 459.67) × 5/9
#Kelvin to Celsius: C = K - 273.15
#Kelvin to Fahrenheit: F = (K × 9/5) - 459.67


temperature = float(input("Enter temperature: "))
tempunit = (input("Enter Kelvin (K), Fahrenheit (F) or Celsius (C): ")).strip().lower()

if tempunit == "c":
    fahrenheit = (temperature * 9/5) + 32
    kelvin = temperature + 273.15
    print(f"Fahrenheit: {fahrenheit}°F")
    print(f"Kelvin: {kelvin}K")
elif tempunit == "f":
    celsius = (temperature - 32) * 5/9
    kelvin = (temperature + 459.67) * 5/9
    print(f"Celsius: {celsius}°C")
    print(f"Kelvin: {kelvin}K")
elif tempunit == "k":
    fahrenheit = (temperature * 9/5) - 459.67
    celsius = temperature - 273.15
    print(f"Celsius: {celsius}°C")
    print(f"Fahrenheit: {fahrenheit}°F")
else:
    print("Invalid temperature unit")