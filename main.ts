/**
 * Created by: Daniel Jeffrey
 * 
 * Created on: Sept 29, 2022
 * 
 * This program calculates the area of a trapezoid with the given values
 */
game.splash("\"We are going to calculate the area of a trapezoid\"")
let A = game.askForNumber("Enter the length of side A in cm:")
let B = game.askForNumber("Enter the length of side B in cm:")
let Height = game.askForNumber("Enter the length for the height in cm:")
game.splash((A + B) / 2, "= (A + B)/2")
let Area = (A + B) / 2 * Height
game.splash("The area of the trapezoid =" + convertToText(Area) + "cm2")
