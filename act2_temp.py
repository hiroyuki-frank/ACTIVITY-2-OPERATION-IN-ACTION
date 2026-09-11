# Name: Frank Magahis
# Section: BMET 2101
# Task 4: Temperature Check

celsius = float(input("Enter temperature in °C: "))

fahrenheit = celsius * 9 / 5 + 32
between = 20 <= celsius <= 30

print("Fahrenheit:", fahrenheit)
print("Between 20 and 30 °C:", between)