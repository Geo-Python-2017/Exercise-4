# Exercise 4: A temperature calculator

In this week's exercise you are asked to create a simple tool that converts temperatures from one temperature-type to another.

After making your changes, you will need to upload these files to GitHub.
The answers to the questions in this week's exercise should be given by modifying the end of this document in the [section titled Answers](#answers).

## Problem 0 - Mid-term course feedback requested
Before you get started on the exercise, we'd like for you to take 5 minutes to provide us with some feedback on how the course is going so far.
This is the first time we're teaching the course in this format, and we would be very pleased to have your honest thoughts (positive or negative) about how things are going.
Feedback is **completely anonymous**.

[**Course feedback e-form**](https://elomake.helsinki.fi/lomakkeet/73256/lomake.html)

## Problem 1 - Temperature calculator

Your first and only task for this week (except giving feedback) is to create a temperature calculator that is used for converting temperatures between Celsius, Fahrenheit and Kelvin. 
You are asked to modify and add functionalities to the functions in [temp_converter.py](temp_converter.py) -file. The temp_converter.py -script is **broken** in its current state, 
thus we want you to fix it by going through the tasks denoted with numbers in the script (1-4). The comments in the script will guide you, and instruct what to do in different parts of the code. 
There are missing parts in the code denoted with _XX_ letters. Modify the script and add your own code to places where letters XX are present.  

In the script you have 6 functions for converting temperatures between different types. Templates for these functions are pre-filled in the script but you need to modify them (three of them). 
We provide you links to materials where you can find the correct mathematical formulas to convert temperatures between different types.  
There is also one function ( _temp_calculator()_ ) that works as a simple user controller that should take 3 parameters as input (you need to modify and add your own code to the function): 

 - **temp** = parameter for passing temperature (numerical)
 - **convert\_from** = parameter that determines whether the **input** temperature is in Celsius, Fahrenheit or in Kelvin (using letters "C", "F" or "K" accordingly)
 - **convert\_to** = parameter that determines whether the **output** temperature is in Celsius, Fahrenheit or in Kelvin (using letters "C", "F" or "K" accordingly)

At the end of the script there are three use cases where different functionalities of the script are tested. If everything in the script is working properly these test cases should produce following
outputs:



_**Note**_:

We hope you can get the whole script working but it is not the end of the world if you cannot get all of its functionalities working. The main point in this exercise is that you get a first 
experience of how more "proper" programs are done by taking advantage of functions.   

### Questions for Problem 1

## General tips

We will add general tips here later. 

# Answers

## Problem 1


**TODO:**

_Temparature converter exercise:_

1. Add functions to temp_converter.py -file:
  - Celsius to Kelvin
  - Fahrenheit to Kelvin
  - Fahrenheit to Celsius
2. Continue adding stuff for calculator.py
  - Student should add third parameter thus having (temp, convert_from, convert_to)
  - Calculator should ask which is the input temperature type ('K' | 'C' | 'F') and to which temperature the value will be converted ('K' | 'C' | 'F')
 
 



