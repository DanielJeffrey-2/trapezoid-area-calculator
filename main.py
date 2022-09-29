"""

Created by: Daniel Jeffrey

Created on: Sept 29, 2022

This program calculates the area of a trapezoid with the given values

"""
game.splash("\"We are going to calculate the area of a trapezoid\"")
A = game.ask_for_number("Enter the length of side A in cm:")
B = game.ask_for_number("Enter the length of side B in cm:")
Height = game.ask_for_number("Enter the length for the height in cm:")
game.splash((A + B) / 2, "= (A + B)/2")
Area = (A + B) / 2 * Height
game.splash("The area of the trapezoid =" + "(A+B)/2 =" + str((A + B) / 2) + "x height =" + convert_to_text(Area) + "cm2")