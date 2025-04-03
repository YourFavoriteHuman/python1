from math import *

while True:
    shape = input("which shape do u want to find volume for?(cube, prism, cyl, pyr, cone, exit): ")

    # Cube: Volume (V) = side³ (s³) 
    # Rectangular Prism (Cuboid): Volume (V) = length × width × height (lwh) 
    # Cylinder: Volume (V) = π × radius² × height (πr²h) 
    # Cone: Volume (V) = (1/3) × π × radius² × height ((1/3)πr²h) 
    # Sphere: Volume (V) = (4/3) × π × radius³ ((4/3)πr³) 
    # Pyramid: Volume (V) = (1/3) × base area × height ((1/3)Bh) 

    if shape == "cube":
        s = int(input("side length: "))
        print("volume =", pow(s, 3))
    elif shape == "prism":
        base = int(input("area of the base: "))
    elif shape == "cyl":
        pass
    elif shape == "pyr":
        pass
    elif shape == "cone":
        pass
    elif shape == "exit":
        break
    else:
        print("invalid shape")
    
    
    
    
    
    