secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# will loop as long as the secret word has not been guessed, and they have not run out of guesses.
# if statement says as long as the count isn't passed the limit ,you can guess
# if guess count reached limit then out_of_guess becomes true and prints the 'you loose statement'
while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOOSE!")
else:
    print("You win!")
