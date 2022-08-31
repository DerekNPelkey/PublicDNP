# Derek Pelkey
# Gravity Calc
# 8/31/22

#calculate time of fall from height above surface
#for local area
import math
g = 9.8066 #Gravity Accel
t = 0 #Time Variable
height = 0 #height

print("average Earth surface gravity = 9.81m/s")
g = float(input("input local gravity acceleration in m/s")) #asks for grav. accel.
height = float(input("What is the Height (m)")) #asks user for height in meters

print("calculating fall time")
assert(g > 0)
assert(height >= 0)
t = math.sqrt(-2*height/-g)  #gravity calculation
print(t, "seconds")