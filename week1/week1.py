#Task 1

print("Robins will wear their feathery fire,")
print("Whistling their whims on a low fence-wire;")
print("And not one will know of the war,")
print("not one")4

#Task 2

print(">Hours in a week:")
print(7*24)
print(">Minutes in a week:")
print(60*7*24)
print(">Seconds in a week:")
print(60*60*7*24)

#Task 3

nickname = input(">What is your nickname?")
print(">")
print(">##Let's review your information##")
print(">Your name:" + name )
print(">Your email:" + email )
print(">Your nickname:" + nickname )
print(">")
print(name + " " + "/" + " " + email + " " + "/" + " " + nickname)

#Task 4

name = input(">Name:")
victim = input(">Victim:")
print(">Thanks for your participation," + " " + name)
print(">" + " " + victim + " " + "Already Died. . .")

#Task 5

name = "Courier"
age = 34
city = "New Vegas"
print(f">Hi {name} , you are {age} years old. You live in {city}.")

#Task 6

name = "Ozan Akyol"
age = 18
skill1 = "python"
level1 = "beginner"
skill2 = "2d art"
level2 = "beginner"
lower = 2000
upper = 3000
print(f">My name is {name}, I am {age} years old")
print(">")
print(">My skills are")
print(f"> - {skill1} ({level1})")
print(f"> - {skill2} ({level2})")
print(">")
print(f">My salary expectation is {lower} - {upper} euros/month")

#Task 7 

number1 = 3
number2 = 5
ans1 = number1 + number2
ans2 = number1 - number2
ans3 = number1 * number2
ans4 = number1 / number2
print(f">number 1 is: {number1}")
print(f">number 2 is: {number2}")
print(f">{number1} + {number2} = {ans1}")
print(f">{number1} - {number2} = {ans2}")
print(f">{number1} * {number2} = {ans3}")
print(f">{number1} / {number2} = {ans4}")

#Task 8

input1 = input("How much do you weigh")
input2 = input("How tall are you")
weight = int(input1)
height = int(input2)
bmi = weight / ((height/100)*(height/100))
print(f"Your BMI is: {bmi}")

#Task 9

game = input(">Game Name:")
release_year = input(">Which year was this game released?")
year = int(release_year)
years_old = (2025 - year)
print(f">Your game is {years_old}")

#Task 10

number1 = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))
product = number1 * number2 * number3
print("The product is", product)