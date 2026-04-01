# 1 - Basic Formula

# celsius = float(input("Enter temperature in Celcius: "))

# fahrenheit = (celsius * 9/5) + 32

# print(f"Celsius = {celsius}^C")
# print(f"Fahrenheit = {fahrenheit}^F")

# 2 - Using a Function

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = float(input("Enter celsius = "))

fahrenheit = celsius_to_fahrenheit(celsius)
back = fahrenheit_to_celsius(fahrenheit)

print(f"Celsius = {celsius}")
print(f"Fahrenheit = {fahrenheit}")
print(f"Back = {back}")
