import json

file = open("C:\\Users\\kariu\\OneDrive\\Desktop\\PLP\\Mini_Project\\data.json","r")
dictionary_data =json.load(file)

def look_word(word):
    if word in dictionary_data:
        return dictionary_data[word]
    else:
        print("Data not found.")

input_word = input("Enter word: ")  

explanation = look_word(input_word) 

print(explanation)     