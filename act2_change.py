# Name: Magahis Frank
# Section: BMET 2101
# Task 1: Change Calculator

amount = int(input("Enter amount in pesos: "))

pesos_100 = amount // 100
remaining = amount % 100

pesos_20 = remaining // 20
remaining = remaining % 20

pesos_5 = remaining // 5
remaining = remaining % 5

pesos_1 = remaining // 1

print("100 pesos:", pesos_100)
print("20 pesos:", pesos_20)
print("5 pesos:", pesos_5)
print("1 peso:", pesos_1)