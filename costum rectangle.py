# // Programming Challenge 3:

# // Create a python program that draws a box in ascii art.

# // Inputs:
# // Ask the user to specify the character to use on the border.
# // Asks the user to specify a character to fill the rectangle with.
# // Asks the user to specify the int width, w
# // Asks the user to specify the int height, h

# // Expected output:

# // Something like 
# // #####
# // #   #
# // #   #
# // #####
# // or
# // %%%
# // %R%
# // %%%

width =int(input(" what do you want the wdith of the rectangle to be? ")) 
height =int(input(" what do you want the hight of the rectangle to be? ")) 
fill =(input(" what do you want the inside of the rectangle to be? "))
border =(input(" what do you want the border of the rectangle to be? "))
g=0
print(width*border)
while  g<height-2:
    print(border+((width-2)*fill)+border)
    g=g+1
print(width*border)
