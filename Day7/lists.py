import cowsay

fruits = ["apple", "banana", "Paris", "date", "elderberry"]
ages = [25, 30, 35, 40, 45]
my_details = ["John", "Doe", 28, "Engineer"]
cars = ["Toyota", "Honda", "Ford", "Chevrolet", "BMW"]
renamed_fruits = fruits[1] = "mango"

cowsay.cow("Hello! Welcome to the world of Python lists!")

print(renamed_fruits)
print(fruits[2])
print(ages[1])
print(my_details[-2])
print(cars[0], cars[-1])

# print(fruits, ages, my_details)