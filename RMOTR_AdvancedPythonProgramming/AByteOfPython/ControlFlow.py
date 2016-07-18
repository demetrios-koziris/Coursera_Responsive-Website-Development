

print("Newlines are indicated by \n")

print("test")

print(not True)

number = 23
running = True

while running:
    guess = input('Enter an integer : ')

    while not str.isdigit(guess):
        print("You must enter an integer")
        guess = input('Enter an integer : ')

    guess = int(guess)
    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
    # Do anything else you want to do here

print('Done')


