#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 23, 2026
# This code first takes a radius value from the user.
# Then it'll calculate the circumference of the circle and display  it.

import constants


def main():

    # Asks for the radius of the circle
    r = int(input("Enter radius of circle. (cm): "))

    # Calculates the circumference
    c = constants.GetTau() * r

    # Displays the calculated circumference
    print("The Circumference of the circle is {}cm".format(c))


if __name__ == "__main__":
    main()
