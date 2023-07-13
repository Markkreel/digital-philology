'''
• Slice the word until first “a”. (Tosc)
• Slice the word so that you get “cana”.
• Can you slice the list so that it’s reversed without using the .reverse() method?
```
word="Toscana"
#???
lst=[0,1,2,3,4]
#???
```
'''

word = "Toscana"

# Slicing until the first "a"
sliced_word_1 = word[:word.index("a")]
print("Sliced word until the first 'a':", sliced_word_1)

# Slicing to get "cana"
sliced_word_2 = word[word.index("c"):word.index("a")+1]
print("Sliced word 'cana':", sliced_word_2)

lst = [0, 1, 2, 3, 4]

# Reversing the list without using .reverse() method
reversed_lst = lst[::-1]
print("Reversed list:", reversed_lst)
