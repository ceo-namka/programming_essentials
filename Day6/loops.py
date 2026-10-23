# i = 0
# while i < 10:
#     print(i)
#     i += 1

# for i in range(10):
#     print(i)

# input_string = input("Enter a string: ",)

# if int(input_string) < 100:
#     print("The string is less than 100.")
# else:
#     print("The string is greater than or equal to 100.")

# sheep_counter = input("sheeps")

# def make_a_bed():
#     print("needs to sleep")
# def take_a_shower():
#     print("needs to take a shower")
# def sleep_and_dream():
#     print("ohh sleeping")
# def feed_the_sheepdogs():
#     print("feeding the sheepdogs")

# if int(sheep_counter) >= 120:
#     make_a_bed()
#     take_a_shower()
#     sleep_and_dream()
# feed_the_sheepdogs()

# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2
# # Print the result
# print("The larger number is:", larger_number)


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the second number: "))

if number1 > number2 and number1 > number3:
    print("this one highest", number1)
elif number2 > number1 and number2 > number3:
    print("this one highest", number2)
elif number3 > number1 and number3 > number2:
    print("highest number:", number3)