student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
file = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_list = {value.letter: value.code for (index, value) in file.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_name = {}
for name in student_dict["student"]:
    nato_name[name] = [nato_list[n.upper()] for n in name]

print(nato_name)

