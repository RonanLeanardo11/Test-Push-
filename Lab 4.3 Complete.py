# Lab 4.3

import tempConverter as tD

# Create a definition called “temperature_converter” that has two keyword and default (to none)
# arguments. This definition should allow the user to enter as an argument EITHER Celsius or Fahrenheit
# (you may assume that the program body will only enter one argument). This must then RETURN the
# temperature converted to the alternative scale.
# Fahrenheit to Celsius = (Fahrenheit – 32) * 0.5666
# Celsius to Fahrenheit = (Celsius * 1.8) + 32
# Test this definition with the following arguments and print the returned value:
# • celsius=50
# • Fahrenheit=102

# Initialise
MenuOption = 0

# Menu
while MenuOption != 3:
    print("\n***** Temperature Converter *****")
    print("-- Choose Menu Option --")
    print("1. Fahrenheit Entry")
    print("2. Celsius Entry")
    print("3. Exit")

    MenuOption = int(input("\nPlease enter Menu Option: "))

    # Fahrenheit Entry
    if MenuOption == 1:
        Fahrenheit = float(input("Please enter Fahrenheit Temp: "))
        tD.temperature_converter(Fahrenheit=Fahrenheit)

    # Celsius Entry
    elif MenuOption == 2:
        Celsius = float(input("Please enter Celsius Temp: "))
        tD.temperature_converter(Celsius=Celsius)

    # Exit
    elif MenuOption == 3:
        pass

