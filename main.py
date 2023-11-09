import json
data = json.load(open('data.json'))

def translatef(word):
    if word in data:
        return data[word]
    else:
        return "The word you entered is not in our dictionary"

word = input("Enter word :")

print(translatef(word))


# SOme changes have been made here to accomplish the branching
# Another changes to the new feature branch
# SOme changes have been made here to accomplish the branching
# SOme changes have been made here to accomplish the branching
# SOme changes have been made here to accomplish the branching