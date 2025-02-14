from math import *


anga = int(input("angle a: "))
b = int(input("b: "))
c = int(input("c: "))

r = sqrt(pow(b,2)+pow(c,2)-(2*(b*c)*cos(degrees(anga))))

print(r)
print(sqrt(pow(12,2)+pow(18,2)-2*(12*18)*cos(degrees(110))))