from os import system, name
from math import *

def clear_screen():
    # For Microsoft Windows
    if name == 'nt':
        _ = system('cls')
    
    # For Mac and Linux (here, os.name is 'posix')
    else:
        _ = system('clear')

#############################################
import math

def law_of_sines(side1, angle1, side2=None, angle2=None):
    """
    Calculates an unknown side or angle of a triangle using the Law of Sines.

    Args:
        side1 (float): Length of a known side.
        angle1 (float): Measure of the angle opposite side1, in degrees.
        side2 (float, optional): Length of a second known side. Defaults to None.
        angle2 (float, optional): Measure of the angle opposite side2, in degrees. Defaults to None.

    Returns:
        float: The length of the unknown side or measure of the unknown angle in degrees.
               Returns None if insufficient information is provided.
    """
    angle1_radians = math.radians(angle1)

    if side2 is None and angle2 is not None:
      angle2_radians = math.radians(angle2)
      side2 = side1 * math.sin(angle2_radians) / math.sin(angle1_radians)
      return side2
    elif side2 is not None and angle2 is None:
      angle2_radians = math.asin(side2 * math.sin(angle1_radians) / side1)
      return math.degrees(angle2_radians)
    else:
        return None



while True:
    clear_screen()
    s1 = int(input("side 1: "))
    a1 = int(input("angle 1: "))
    
    try:
        s2 = int(input("side 2: "))
    except ValueError:
        s2 = None

    try:
        a2 = int(input("angle 2: "))
    except ValueError:
        a2 = None
    
    print(law_of_sines(s1,a1,s2,a2))
    input()