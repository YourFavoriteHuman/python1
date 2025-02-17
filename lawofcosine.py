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

def law_of_cosines_side(a, b, C):
  """
  Calculates the length of the side opposite angle C using the law of cosines.

  Args:
    a: Length of side a.
    b: Length of side b.
    C: Angle C in degrees.

  Returns:
    Length of side c.
  """
  C_radians = math.radians(C)
  c_squared = a**2 + b**2 - 2 * a * b * math.cos(C_radians)
  return math.sqrt(c_squared)

def law_of_cosines_angle(a, b, c):
  """
  Calculates the angle opposite side c using the law of cosines.

  Args:
    a: Length of side a.
    b: Length of side b.
    c: Length of side c.

  Returns:
    Angle C in degrees.
  """
  C_radians = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
  return math.degrees(C_radians)


while True:
    clear_screen()
    aors = input("find angle or side? (a/s): ")
    if aors == 's':
        anga = int(input("angle a: "))
        b = int(input("b: "))
        # print("b:", b)
        
        c = int(input("c: "))
        # print("c:", c)

        b2 = pow(b,2)
        c2 = pow(c,2)

        r = sqrt(b2+c2-2*(b*c)*degrees(cos(anga)))

        print(law_of_cosines_side(b,c,anga))
        input()
    elif aors == 'a':
        sa = int(input("side a: "))
        sb = int(input("side b: "))
        sc = int(input("side c: "))
        print(law_of_cosines_angle(sa,sb,sc))
        input()