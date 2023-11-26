 # Math quiz using a random number generator

   # 11/24/23

   # CTI-110 P5HW - Math Quiz

   # Mahamed Abdel

   #



import random

def generate_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtract_numbers(num1, num2):
    return num1 - num2

def main():
    print("Welcome to Math Quiz")
    while True:
        print("\nMAIN MENU")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")

        choice = input("Please choose one of the menu options: ")

        if choice == "1":
            num1, num2 = generate_numbers()
            result = add_numbers(num1, num2)
            print(f"\n{num1} + {num2}")
            guess = int(input("Enter your answer: "))
            attempts = 1

            while guess != result:
                if guess < result:
                    print("Sorry, guess is too low.")
                else:
                    print("Sorry, guess is too high.")
                guess = int(input("Try again: "))
                attempts += 1

            print(f"Congratulations!!!! Your answer is correct.")
            print(f"Number of guesses: {attempts}")

        elif choice == "2":
            num1, num2 = generate_numbers()
            result = subtract_numbers(num1, num2)
            print(f"\n{num1} - {num2}")
            guess = int(input("Enter your answer: "))

            while guess != result:
                print("Sorry, guess is incorrect.")
                guess = int(input("Try again: "))

            print(f"Congratulations!!!! Your answer is correct.")

        elif choice == "3":
            print("\nThank you for playing...\nBye! !")
            break

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.")

if __name__ == '__main__':
    main()
