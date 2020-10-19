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


def convert_dog(string):

    """Converts passed in string into dog language and returns it

    Arguments:
        string (str): The text you want to convert

    Returns:
        str: Converted Text
    """

    letters = [letter for letter in string]
    final = ""

    # print(letters)

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

def convert_en(string):

    """Converts text to english from Dog Language

    Arguments:
        string (str): Text you want to convert in dog language 

    Returns:
        str: Converted text from dog to english
    """

    split = string.split()

    current_word = ""
    final = ""

    for woof in split:
        if not woof.endswith("."):
            current_word += f"{woof} "
            # print(current_word)

        elif woof.endswith(".."):
            current_word += woof[:-2]
            word = language.index(current_word)
            # print(current_word)

            final += f"{english[word]} "
            current_word = ""

        else:
            current_word += f"{woof[:-1]}"
            letter = language.index(current_word)
            current_word = ""
            # print(current_word)

            final += english[letter]

    return final
    

if __name__ == "__main__":
    
    translate = input("Translate this to dog: ")

    sent = convert_dog(translate)

    print(sent)

    print(convert_en(sent))