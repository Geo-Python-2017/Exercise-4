# Exercise 4: Classifying and converting temperatures

In this week's exercise you are asked to create a simple tool that converts temperatures from one temperature-type to another.

After making your changes, you will need to upload these files to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

## Problem 0 - Mid-term course feedback requested
Before you get started on the exercise, we'd like for you to take 5 minutes to provide us with some feedback on how the course is going so far.
This is the first time we're teaching the course in this format, and we would be very pleased to have your honest thoughts (positive or negative) about how things are going.
Feedback is **completely anonymous**.

[**Course feedback e-form**](https://elomake.helsinki.fi/lomakkeet/73256/lomake.html)

## Problem 1 - Simple temperature calculator (6 points)

In the first problem your aim is to create a function that converts the input temperature from Fahrenheit to Celsius.
Create a script called `converter.py` where you should write your code for Problem 1.

You should do following (also criteria for grading):

  - create a function called `fahrToCelsius` into `converter.py`
  - function should have one input parameter called `temp_f`
  - inside the function, create a variable called `converted_temp` where you should store the conversion result (i.e. the input Fahrenheit temperature converted to Celsius)
  - The conversion formula from Fahrenheit to Celsius is:
       - ![](img/Fahrenheit_to_Celsius_formula.PNG)
  - return the converted value from the function back to the user
  - test and use your newly created function by printing out the results for following questions:
     - What is 48 Fahrenheits in Celsius?
     - What about 71 Fahrenheits in Celsius?
  - Comment your code and add a docstring that explains how to use your `fahrToCelsius` function (i.e. you should write the purpose of the function, parameters, and return values)
  - Upload and commit your script `converter.py` to your own GitHub Exercise 4 repository

If everything in your script is working properly the following test case should work:

  ```python
  >>> print("32 Fahrenheits is in Celsius:", fahrToCelsius(32))
  32 Fahrenheits is in Celsius: 0.0
  ```

## Problem 2 - Temperature classifier (7 points)

In the [last week's exercise (Problem 2)](https://github.com/Geo-Python-2017/Exercise-3) we practiced how to classify temperatures
into four different classes (cold, slippery, comfortable, warm). Let's continue working with the same idea.

Create another script called `classify.py` where you should write your code for Problem 2.

## Problem 3 - Classify temperatures (7 points)





## Problem 2 -

Your first and only task for this week (except giving feedback) is to create a temperature calculator that is used for converting temperatures between Celsius, Fahrenheit and Kelvin.
You are asked to modify and add functionalities to the functions in [temp_converter.py](temp_converter.py) -file. The temp_converter.py -script is **broken** in its current state, 
thus we want you to fix it by going through the tasks denoted with numbers in the script (1-4). The comments in the script will guide you, and instruct what to do in different parts of the code. 
There are missing parts in the code denoted with _**XX**_ letters. Modify the script and add your own code to places where letters _**XX**_ are present.  

In the script you have 6 functions for converting temperatures between different types. Templates for these functions are pre-filled in the script but you need to modify them (three of them). 
We provide you links to materials where you can find the correct mathematical formulas to convert temperatures between different types.  
There is also one function ( _temp_calculator()_ ) that works as a simple user controller that should take 3 parameters as input (you need to modify and add your own code to the function): 

 - **temp** = parameter for passing temperature (numerical)
 - **convert\_from** = parameter that determines whether the **input** temperature is in Celsius, Fahrenheit or in Kelvin (using letters "C", "F" or "K" accordingly)
 - **convert\_to** = parameter that determines whether the **output** temperature is in Celsius, Fahrenheit or in Kelvin (using letters "C", "F" or "K" accordingly)

At the end of the script there are three use cases where different functionalities of the script are tested. If everything in the script is working properly these test cases should produce following
outputs:

  ```python
  >>> print("32 Fahrenheits is in Celsius:", fahr_to_celsius(32))
  32 Fahrenheits is in Celsius: 0.0
  
  >>> print("100 Celsius is in Kelvin:", celsius_to_kelvin(temp_c=100))
  100 Celsius is in Kelvin: 373.15
  
  >>> print("50 Fahrenheits is in Kelvin:", fahr_to_kelvin(temp_f=50))
  50 Fahrenheits is in Kelvin: 283.15000000000003
  
  >>> temperature = 30
  >>> converted_temp = temp_calculator(temp=temperature, convert_from="C", convert_to="F")
  >>> print("Temperature %s in Celsius is %s in Fahrenheit" % (temperature, converted_temp))
  Temperature 30 in Celsius is 86.0 in Fahrenheit
  
  >>> temperature = 50
  >>> converted_temp = temp_calculator(temp=temperature, convert_from="K", convert_to="F")
  >>> print("Temperature %s in Kelvin is %s in Fahrenheit" % (temperature, converted_temp))
  Temperature 50 in Kelvin is -369.66999999999996 in Fahrenheit

  >>> temperature = -20
  >>> converted_temp = temp_calculator(temp=temperature, convert_from="F", convert_to="C")
  >>> print("Temperature %s in Fahrenheit is %s in Celsius" % (temperature, converted_temp))
  Temperature -20 in Fahrenheit is -28.88888888888889 in Celsius
  ```

**Upload your updated _temp_converter.py_ -script to your personal GitHub repository.** 
  
_**Note**_:

We hope that you can get the whole script working but _it is not the end of the world_ if you cannot fix all of its functionalities. The main point in this exercise is that you get a first 
experience of how more "proper" programs can be created by taking advantage of functions.   

### Questions for Problem 1

In addition to providing your updated temp_converter.py script, we wish you to think and answer to following questions based on the materials and ideas that you learned during the lecture:
  
  1. Is the concept of function clear to you? If not, what do you not understand?
  2. What are the benefits of using functions in your script?
  3. Does it matter in which order the functions are written in a script? If you think it does, why?
   

## General tips

We will add general tips here later. 

# Answers

Upload your updated _temp_converter.py_ -script to your personal GitHub repository.

## Problem 1 - Answers to questions

### 1. 

### 2.

### 3. 




