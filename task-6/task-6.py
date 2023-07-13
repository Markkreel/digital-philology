'''
Create tuples of colors (String) and their HEX representation (#ffffff-white ,String).
• Combine the tuples to be a dictionary of colors references by the names and returning HEX
values
'''

# Creating the color tuples
color_tuples = [
    ("white", "#ffffff"),
    ("red", "#ff0000"),
    ("green", "#00ff00"),
    ("blue", "#0000ff"),
]

# Combining the tuples into a dictionary
color_dict = dict(color_tuples)

print(color_dict)
