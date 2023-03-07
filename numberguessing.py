#first application (nearly) by myself sun 26th feb

x = 3
number = int(input("Guess my number between 1-10: "))
while x!= number:
    if number > 10:
        print("Please enter a number below 11")
    if number <= 2:
        print("Higher") 
        number = int(input("Guess number again: ",))
    if number >= 4:
        print("Lower")
        number = int(input("Guess number again: ",))
    if number == 3:
        print("You got it! You're a star.")