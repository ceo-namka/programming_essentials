# hundred = 100
# hundred = 200 + 200

# print(hundred)

# a = 2.0
# b = 3.0 
# c = (a ** 2 + b ** 2) ** 0.5

# print(c)

# john = 6
# mary = 4
# adam = 8

# total_apples = john + mary + adam

# print(john, mary, adam, sep=", ")
# print(total_apples)

# j = 2
# i = 4
# var = 10
# rem = 5
# x = 3

# i += 2 * j
# var /= 2
# rem %= 10
# j -= i + var + rem
# x **= 2

# print(i, j, var, rem, x, sep=", ")

# miles = 1 
# kilometers = 1.61

# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers / 1.61

# print("miles to km :", miles, "miles is", round(miles_to_kilometers, 2), "km")
# print("km to miles :", kilometers, "km is", round(kilometers_to_miles, 2), "miles")

# x = 2

# print(3 * x ** 3 + 2 * x ** 2 + 5 * x + 7)

# print("hey")

# question = input()
# possibleAnswers = ["im", "I'm", "I am", "i'm", "i am"]

# words = question.split()

# for i in range(len(words)):
#     if words[i] in possibleAnswers:
#         words[i] = "you are"
#     if words[i].lower() == "i" and i + 1 < len(words) and words[i + 1].lower() == "am":
#         words[i] = "you"
#         words[i + 1] = "are"

# cleanedQuestion = " ".join(words) 

# print("ok", cleanedQuestion, "i see...")

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# hypo = (leg_a**2 + leg_b**2) ** .5
# print("Hypotenuse length is", hypo)

# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")

print("+" + "-" * 10 + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")