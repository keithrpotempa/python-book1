my_family = {
    "sister": {
        "name": "Krista",
        "age": 42
    },
    "mother": {
        "name": "Cathie",
        "age": 70
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old

for member, properties in my_family.items():
  sentence = f"{properties['name']} is my {member} and is {properties['age']} years old"
  print(sentence)