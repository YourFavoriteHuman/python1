from math import *

while True:
    shape = input("which shape do u want to find volume for?(cube, prism, cyl, pyr, cone, sphere, exit): ")

    # Cube: Volume (V) = side³ (s³) 
    # Rectangular Prism (Cuboid): Volume (V) = length × width × height (lwh) 
    # Cylinder: Volume (V) = π × radius² × height (πr²h) 
    # Cone: Volume (V) = (1/3) × π × radius² × height ((1/3)πr²h) 
    # Sphere: Volume (V) = (4/3) × π × radius³ ((4/3)πr³) 
    # Pyramid: Volume (V) = (1/3) × base area × height ((1/3)Bh) 

    if shape == "cube":
        s = float(input("side length: "))
        print("volume =", pow(s, 3))
    elif shape == "prism":
        base = float(input("area of the base: "))
        height = float(input("height of prism: "))
        print("volume =", (base*height))
    elif shape == "cyl":
        height = float(input("height of cylinder: "))
        radius = float(input("radius of prism base: "))
        print("volume =", (pi * pow(radius, 2) * height))
    elif shape == "pyr":
        base = float(input("area of the base: "))
        height = float(input("height of pyramid: "))
        print("volume =", ((1/3)*base*height))
    elif shape == "cone":
        height = float(input("height of cone: "))
        radius = float(input("radius of cone base: "))
        print("volume =", ((1/3) * pi * pow(radius, 2) * height))
    elif shape == "sphere":
        radius = float(input("radius of sphere: "))
        print("volume =", ((4/3) * pi * pow(radius, 3)))
    elif shape == "exit":
        break
    else:
        print("invalid shape")
    
    
    
    
    
    