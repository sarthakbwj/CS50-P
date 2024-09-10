# taking an input from the user asking the mass of an object (in kg).
m = int(input("Enter a mass (in kg): "))
# storing the value of speed of light (in m/s being taken the power of two) in a variable "c".
c = pow ( 300000000 , 2 )
# storing the calculated value of the energy in a variable "e".
e = (m*c)
# printing the varialble "e" along with a string to make it easy for the user to read.
print ("e = m*c** = ",e,"joules.")



