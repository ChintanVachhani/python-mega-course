import json
import difflib as dl

data = json.load(open('data.json'))


def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(dl.get_close_matches(word, data.keys())) > 0:
        answer = input(
            "Did you mean '%s' instead? Enter 'Y' if yes, 'N' if no: " % dl.get_close_matches(word, data.keys())[0])
        if answer.upper() == "Y":
            return data[dl.get_close_matches(word, data.keys())[0]]
        elif answer.upper() == "N":
            return "The word doesn't exist. Please check again."
        else:
            return "I couldn't understand the entry."
    else:
        return "The word doesn't exist. Please check again."


response = define(input("Enter a word: "))

if type(response) == list:
    print("Definition(s): ")
    for item in response:
        print("\t- ", item)
else:
    print(response)
