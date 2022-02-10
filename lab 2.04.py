'''
###########################
Lab 2.04
###########################
1. In your notebook
For each example below, predict what will be printed. Run the program and write down the output in your notebook.

Example 1
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[0])
    print(a[3])

    prediction: 'a', 'd'                                           
    actual: a , d

Example 2
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 3])

    prediction: d
    actual: c

Example 3
    a = ['a', 'b', 'c', 'd', 'e']
    print(a[len(a) - 6])

    prediction: a
    actual: e

Example 4
    a = ['a', 'b', 'c', 'd', 'e']
    a[3] = 'haha'
    print(a)

    prediction: haha
    actual: ['a', 'b', 'c', 'haha', 'e']

2. Create this game again using lists and indexes
--------------------------------------------------
Declare 10 prizes (prize0, prize1, prize2 at the top of your file), but store them all in a list.

User picks a number.

Print prize associated with the door user picked.

3. Create a quiz
--------------------------------------------------
Create a food quiz using lists and indexes.

List of 6 different foods.

Ask the user 8 vague questions to find out what their favorite food is using the list.

Update the score and print their top 2 favorite foods.

Hint: Use a search engine to find the largest number in a python list.

----------------------
​Starter code here​:
----------------------
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1

##############################
Together in class:
##############################
Research nested lists and work through the following Examples:

Bonus Example 1
a = ['a', 'b', 'c', ['d', 'e']]
print(len(a))
Bonus Example 2
a = ['a', 'b', 'c', ['d', 'e']]
b = a[3]
print(b)
Bonus - In your Notebook
How would you access d from the list a?
'''
'''
a = ['dog', 'cat', '$100', 'lion', ' $500', 'nothing', 'free meal', '$1,000', 'nothing', '$10,000']
choose = input()
choose = int(choose)
print(a[choose])
'''
food = ['donuts', 'pancakes', 'bacon', 'waffles','eggs','baggles']
score = [0,0,0,0,0,0]

print('Please answer each questions with "y" for "yes" and "n" for "no."')
user_input = input('Do you like food with holes? ')
if user_input == 'y':
  score[0] = score[0] + 1
  score[5] = score[5] + 1
if user_input == 'n':
    user_input = input("Does your favorite food come from an animal?")
if user_input == 'y':
    score[2] = score[2] + 1
    score[4] = score[4] + 1
user_input = input("Is your food yellow and white?")
if user_input == 'y':
    score[4] = score[4] + 1
    print("Your favorite food are eggs.")
    print("Your second favorite food is bacon.")
if user_input == 'n':
    score[2] = score[2] + 1
    print("Your favorite food is bacon.")
    print("Your second favorite food are eggs.")
user_input = input('Do you put cream cheese on this food?')
if user_input == 'y':
    score[5] = score[5] + 1
    print("Your favorite food is a baggle.")
    print("Your second favorite food is a donut.")
elif user_input == 'n':
    score[0] = score[0] + 1
    print("Your favorite food is a donut.")
    print("Your second favorite food is a baggle.")