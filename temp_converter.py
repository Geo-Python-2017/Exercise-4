#!/usr/bin/env python3
"""temp_converter.py

This simple script consist of functions used for converting temperatures between Celsius, Fahrenheit and Kelvin and a
simple 'temp_calculator' function that can be used for converting temperatures from specific input temperature to specified
output temperature.

Limitations:
This script does not work if the missing parts are not filled and fixed. Missing places are denoted with numbered
comments and/or with XX letters.

Usage: ./temp_converter.py

Henrikki Tenkanen - 25.9.2016

"""

def celsius_to_fahr(temp_c):
    """Function to convert Celsius temperature to Fahrenheit."""
    return 9/5 * temp_c + 32

def kelvin_to_celsius(temp_k):
    """Function to convert Kelvin temperature to Celsius."""
    return temp_k - 273.15

def kelvin_to_fahrenheit(temp_k):
    """Function to convert Kelvin temperature to Fahrenheit."""
    # Kelvin in celsius
    temp_c = kelvin_to_celsius(temp_k)
    # Celsius in Fahrenheit
    temp_f = celsius_to_fahr(temp_c)
    # Return the result
    return temp_f

# 1.
def celsius_to_kelvin(temp_c):
    # 1.1 Add functionality here
    # Function should convert input Celsius temperature to Kelvin and return that value
    # See conversion formula from here: http://www.rapidtables.com/convert/temperature/how-celsius-to-kelvin.htm
    return

# 2.
def fahr_to_celsius(temp_f):
    # 2.1 Add functionality here
    # Function should convert input Fahrenheit temperature to Celsius and return that value
    # See conversion formula from here: http://www.rapidtables.com/convert/temperature/how-fahrenheit-to-celsius.htm
    return

# 3.
def fahr_to_kelvin(temp_f):
    # 3.1 Add functionality here
    # Function should convert input Fahrenheit temperature to Kelvin and return that value
    # See conversion formula from here: http://www.rapidtables.com/convert/temperature/how-fahrenheit-to-kelvin.htm
    return

# 4.

# NOTICE: The function below is BROKEN and you need to fix it by modifying the function and
# adding missing parts to places (denoted with XX -letters) where instructed (with comments)

# 4.1: Modify the temp_calculator function and add a third parameter called 'convert_from'
def temp_calculator(temp, XX, convert_to):
    # 4.2: Add description about the new 'convert_from' parameter to text below (see description of 'convert_to' and use that as a template):
    """
    Function for converting temperatures between Celsius, Kelvin and Fahrenheit.

    Parameters:
    -----------
    temp: Temperature in Kelvin <numerical>
    convert_to: Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Possible values: 'C' | 'F'
    """

    # Check if input temperature is in Kelving
    if convert_from == "K":
        # Check if user wants the Kelvin temperature as Celsius
        if convert_to == "C":
            # Convert the value to Celsius using dedicated function for the task that we imported from another script
            converted_temp = kelvin_to_celsius(temp_k=temp)
        elif convert_to == "F":
            # Convert the value to Fahrenheit using dedicated function for the task that we imported from another script
            converted_temp = kelvin_to_fahrenheit(temp_k=temp)
        else:
            # If other values are passed to 'convert_to' column, return None as result
            converted_temp = None
        # Return the result
        return converted_temp

    # 4.3 Add a condition to check if input temperature (i.e. 'convert_from') is in Celsius ("C")
    elif convert_from == XX :
        # Check if user wants the Celsius temperature in Fahrenheit
        if convert_to == "F":
            converted_temp = celsius_to_fahr(temp)

        # 4.3.1 Add conditional statement and conversion to convert Celsius to Kelvin
        elif XX :
            converted_temp = XX
        else:
            # If other values are passed to 'convert_to' column, return None as result
            converted_temp = None
        # 4.3.2 Add a return statement for returning the value in 'converted_temp' -variable.
        XX

    # 4.4 Add a condition to check if input temperature (i.e. 'convert_from') is in Fahrenheit ("F")
    elif XX :
        # 4.3.1 Add conditional statement and conversion to convert Fahrenheit to Celsius
        if XX :
            converted_temp = XX
        # 4.3.2 Add conditional statement and conversion to convert Fahrenheit to Kelvin
        elif XX :
            converted_temp = XX
        else:
            # If other values are passed to 'convert_to' column, return None as result
            converted_temp = None

    # If input temperature ('convert_from') is something else than ('C' | 'K' | 'F') send a notification about the issue.
    else:
        print("Input temperature type", convert_from, "was not detected. Possible values are 'C' for Celsius, 'K' for Kelvin and 'F' for Fahrenheit.")

# 5. Testing the functions
# ------------------------

# 5.1 Test prints for new functions
print("32 Fahrenheits is in Celsius:", fahr_to_celsius(32))
print("100 Celsius is in Kelvin:", celsius_to_kelvin(temp_c=100))
print("50 Fahrenheits is in Kelvin:", fahr_to_kelvin(temp_f=50))

# 5.2 Testing temp_converter -function (not working unless the function has been fixed)
# 1.
temperature = 30
converted_temp = temp_calculator(temp=temperature, convert_from="C", convert_to="F")
print("Temperature %s in Celsius is %s in Fahrenheit" % (temperature, converted_temp))

# 2.
temperature = 50
converted_temp = temp_calculator(temp=temperature, convert_from="K", convert_to="F")
print("Temperature %s in Kelvin is %s in Fahrenheit" % (temperature, converted_temp))

# 3.
temperature = -20
converted_temp = temp_calculator(temp=temperature, convert_from="F", convert_to="C")
print("Temperature %s in Fahrenheit is %s in Celsius" % (temperature, converted_temp))
