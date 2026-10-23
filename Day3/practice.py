# name = "Namka"
# age = 20
# print("My name is " + name + " and I am " + str(age) + " years old.")

# province = "Ontario"
# continent = "North America"
# print(province, continent, sep=" is in ")

# print("Hello\nWorld")
# print("Name:\tEvelyn")
# print("She said \"Hello\"")

# test1 = "hello"
# test2 = "world"
# print(test1, test2, sep="-",end="!")

# name = input("What is your name? ")
# age = input("What is your age? ")
# print("My name is " + name + " and I am " + str(age) + " years old.")

# what = input("What is your name? ")
# hey = input("What is your age? ")

# def test(name, age): (
#     print(f"Here is your name: {name} \n  your age is {age} years old.")
# )

# test(what, hey)

# print("Python", "Programming", sep="-")
# print("2026", "09", "27", sep="/")
# print("Ireland", "Nigeria", "UK", sep=", ")
# print("A", "B", "C", sep="")

# print(f"{'Name':<10}{'Age':<5}{'Country'}")
# print(f"{'Evelyn':<10}{30:<5}{'Ireland'}")
# print(f"{'John':<10}{25:<5}{'Nigeria'}")

# price = 25.255232
# print(f"Price is: ${price:.10f}")

# percentage = 0.1324242
# print(f"Rate is: {percentage:.5%}")

from datetime import date

def student_profile(name, course, location, price):
    
    today = date.today()

    print("PYTHON LEARNING PROFILE ", sep="\n"),
    print(f"Name: {name}"),
    print(f"Course: {course}"),
    print(f"Location: {location}")
    print(f"Price is: {price:.2f} and  {price:.5%}")
    print(f"Date: {today:%d/%m/%y}")


student_profile("Evelyn", "Python Programming", "Ireland", 24.2354242 )

