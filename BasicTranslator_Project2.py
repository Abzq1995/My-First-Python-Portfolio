def translate(phrase):
    translation = ""
# this code will change any vowel to a g or G , depending on if it is upper case or lower case
# if no vowel present then it just keep the letter as it is
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
