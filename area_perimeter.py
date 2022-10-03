#!/usr/bin/env python3
# Created by: Samuel Nkongolo
# Created on: Oct. 1, 2022
# This program asks the user for the length of a hexagon
# calculates and displays the area and
# perimeter.
import math
from re import A


def main():
    # Get the length of a side of a hexagon
    print("Today we will calculate the area and")
    print("perimeter of a Hexagon")
    length = float(input("Enter the length (mm): "))

    # calculating the area and perimeter of a hexagon given the length, using formulas
    area = (3 * math.sqrt(3) * length**2) / 2
    perimeter = length * 6

    # Displaying the are and perimeter to the user
    print("")

    print("Area = {} mm^2".format(area))
    print("Perimeter = {} mm".format(perimeter))


if __name__ == "__main__":
    main()
