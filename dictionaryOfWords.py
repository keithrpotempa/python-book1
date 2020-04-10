"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

word_definitions["Awesome"] = "The feeling of students when they are learning Python"
word_definitions["Sesquipedalian"] = "characterized by long words; long-winded."
word_definitions["Poodle"] = "a dog of a breed (of which there are several varieties) with a curly coat that is often ornamentally clipped. Poodle breeds are classified by size."
word_definitions["Wanton"] = "(of a cruel or violent action) deliberate and unprovoked."

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""

# print(word_definitions["Awesome"])
# print(word_definitions["Wanton"])

"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""

for (word,definition) in word_definitions.items():
    print(f'The definition of {word} is: {definition}')