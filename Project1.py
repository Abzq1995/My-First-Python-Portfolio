#Excercise 1
first = "Good"
second = "Day"
name = "Abdul"
print(first + " " + second + " " + name)

print(100 * '_')

#Excercise 2 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("it is a pleasure to meet you , " + first_name + " " + last_name)

print(100 * '_')

#Excercise 3
'# by putting input the user will enter a number and decimal to be used as number1 and number2 respectively'
number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")
'# when putting int before number 1 it will turn the string into a  whole number value'
integer_number = int(number1)
'# by putting float before number2 it will change the string(float_number) to a float/decimal value'
float_number = float(number2)
'#by putting int and round before the float_number it will round the decimal value to whole value number'
round_number = int(round(float_number))
final_number = int(input("Enter a number:"))
final_number = final_number/round_number
print(number1)
print(number2)
print(round_number)
print(final_number)

print(100 * '_')

#Excercise 4
dog_name = input("Enter your dogs name: ")
dog_breed = input("Enter your dogs breed: ")
dog_age = int(input("Enter your dogs age:"))
bark = True
tweet = False

print("My pet is called", dog_name, ". They are a", dog_breed, "and they are", dog_age, "years old.")
print("Statement:", dog_name, "barks:", bark)
print("Statement:", dog_name, "tweets:", tweet)

print(100 * '_')

#Excercise 5
chemistry = int(input("Enter your Chemistry mark here: "))
biology = int(input("Enter your Biology mark here: "))
physics = int(input("Enter your Physics mark here: "))

average = (chemistry + biology + physics) / 3

print()
if average > 84:
    print("Based on your average mark of", average, ", you've earned a distinction!")

if 64 < average < 85:
    print("Based on your average mark of", average, ", you've earned a pass!")

if average < 65:
    print("Based on your average mark of", average, ", you have unfortunately failed...")


