# num = int

# while num != 8:
#     num = int(input("Guess a number between 1 and 10 until you get it right :"))
#     if num == 8:
#         print("Well guessed!")

num = 7
guess = int(input("Guess a number between 1 and 10 until you get it right :"))

while guess != num:
    guess = int(input("Guess a number between 1 and 10 until you get it right :"))

print("Well guessed!")