'''
• Start with our original XML and transform it programmatically, such that all <play> elements
are listed directly under the <plays> root element. Their category should be included as a
new attribute. The original category elements should be removed.

```
<plays>
<play year="1602" category="comedy">All's Well That Ends Well</play>
...
<play year="1593" category="tragedy">Titus Andronicus</play>
</plays>
```
'''

import xml.etree.ElementTree as ET

# Define the XML string
plays_xml = """<plays completeness="incomplete">
<comedies>
    <play year="1602">All's Well That Ends Well</play>
    <play year="1595">Midsummer Night's Dream</play>
</comedies>
<histories>
    <play year="1598">Henry V</play>
    <play year="1592">Richard III</play>
</histories>
<tragedies>
    <play year="1605">Macbeth</play>
    <play year="1593">Titus Andronicus</play>
</tragedies>
</plays>
"""

root = ET.fromstring(plays_xml)

new_root = ET.Element("plays")

# Iterate over the existing categories
for category in root:
    # Iterate over the play elements within each category
    for play in category:
        # Create a new play element under the new root
        new_play = ET.SubElement(new_root, "play")
        
        # Get the 'year' attribute to the new play element
        new_play.set("year", play.get("year")) # type: ignore (Due to error warnings that's not true, I need to put "type: ignore")
        
        # Set the 'category' attribute to the category of the play
        new_play.set("category", category.tag)
        
        # Set the text of the new play element to the play's text
        new_play.text = play.text

# Create a new ElementTree with the new root element
new_tree = ET.ElementTree(new_root)

file_path = "/home/mark/Documents/digital-philology/task-16/new_plays.xml" # Your desired directory for the new .xml file

new_tree.write(file_path)

print("File created successfully at:", file_path) # Progress clarification
