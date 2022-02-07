'''
##########################################
Lab 2.03 - Game Show
##########################################
In your Notebook
Follow the flow of execution in the following programs and predict what will happen for each
one
---------------------------------------
Example 1
---------------------------------------
a = input("What... is your quest")
b = "to seek the holy grail"
if a != b:
    print("Go On. Off you go")
else:
    b = input("What...is the air-speed velocity of an unladen swallow?")
    if b == "What do you mean? An African or European swallow?":
        print("I don't know that...AHHH [Bridgekeeper was thrown over bridge]")
    else:
        print("[you were thrown over bridge]")

Prediction: program will work and execute as needed
Actual: program worked but you must type the exact quotes or it will just return "Go on. Off you go."

---------------------------------------
Example 2
---------------------------------------
user_input = input("What is your favorite color")
if user_input == 'blue':
    print("Blueskadoo")
elif user_input == "red":
    print("Roses are red!")
elif user_input == "yellow":
    print("Mellow Yellow")
elif user_input == "green":
    print("Green Machine")
elif user_input == "orange":
    print("Orange you glad I didn't say banana.")
elif user_input == "black":
    print("I see a red door and I want it painted black")
elif user_input == "purple":
    print("And we'll never be royalllssss")
elif user_input == "pink":
    print("Pinky- and the Brain")
else:
    print("I don't recognize that color. Is it even...??")

Prediction: program works and outputs correctly
Actual: program worked

---------------------------------------
In your Notebook
---------------------------------------
Translate this Snap! program into a Python program
***Refer to the image provided on Moodle located below the Lab 2.03 link***
Write program below:

---------------------------------------
Create a game show program
---------------------------------------
Declare 10 prizes (prize1, prize2, prize 3 at the top of your file)
User picks a number
The prize corresponding with that door is printed for the user.
Write code below the multiline comment
'''
'''
# get 3 sides of a traignle from user
x = int(input("What is x?"))
y = int(input("What is y?"))
z = int(input("What is z?"))

# can it be a triangle
if x + y > z and x + z > y and y + z > x:
    print(f"perimeter of the triangle is: {x + y + z}")
    
    # is it a right triangle
    if x ** 2 + y ** 2 == z ** 2:
        print("This is a right triangle")

    # determine if isoscelese, scalene, equilateral
    if x == y and y == z:
        print("This is an equilsteral triangle.")
    elif x == y or z == y or x == z:
        print("This is an isosceles traingle.")
    else:
        print("This is a scalene triangle.")
else:
    print("Sorry, these inputs do not make a triangle")
'''
list1 = ['dog','cat','tiger','lion','zebra', 'elephant','whale','dolphin','$10,000']
x = int(input("Pick a number 0-9"))
print({list1})