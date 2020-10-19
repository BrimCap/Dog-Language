language = [
    "woof",
    "woof woof",
    "woof woof woof",
    "wowoof",
    "wowowoof",
    "wowowoof woof",
    "wowowoof woof woof",
    "wowoof woof",
    "wowoof woof woof",
    "woowoof",
    "woowoof woof",
    "woowoof woof woof",
    "woowowoof",
    "woowowoof woof",
    "woowowoof woof woof",
    "worf",
    "worf woof",
    "worf woof woof",
    "bark",
    "bark woof",
    "bark woof woof",
    "bark bark",
    "bark bark woof",
    "bark bark woof woof",
    "bark bark woof woof woof",
    "bark bark bark"
]

english = "abcdefghijklmnopqrstuvwxyz"


def convert(string):

    """Converts passed in string into dog language and returns it

    Arguments:
        string (str): The text you want to convert

    Returns:
        str: Converted Text
    """

    letters = [letter for letter in string]
    final = ""

    print(letters)

    for i, letter in enumerate(letters):
        if letter != " ":
            alphabet = english.find(letter)
            final += language[alphabet]

            if i == len(letters) - 1 or letters[i+1] == " ":
                final += ".. "

            else:
                final += ". "

        else:
            continue

    return final
    

if __name__ == "__main__":
    
    translate = input("Translate this to dog: ")

    print(convert(translate))