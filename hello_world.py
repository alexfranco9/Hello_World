# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name,"!")	# with a comma
print("Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", 42,"!")	# with a comma
print("Hello " + str(42) + "!")   # with a +	-- this one should give us an error!
# for this one we would use print("Hello" + str(42) + "!") without the str(42) we get an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {}.".format(fave_food1)) # with .format()
print(f"I love to eat {fave_food2}.") # with an f string

# bonus 
my_food = "hamburgers"
my_food1 = "pasta"

print("I love to eat {} and {}.".format(my_food, my_food1))

more_food = "steak"
more_food1 = "chicken sandwich"

print(f"I love to eat {more_food} and {more_food1}.")

first_name = "alexander"
last_name = "FRANCO"
print(str.capitalize(first_name))
print(str.lower(last_name))