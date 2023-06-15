wrd = "Toscana"

# Slice the word until the first "a"
sliced_word_1 = wrd[:wrd.index("a")]
print("Sliced word until first 'a':", sliced_word_1)

# Slice the word to get "cana"
sliced_word_2 = wrd[wrd.index("c"):wrd.index("a")+1]
print("Sliced word 'cana':", sliced_word_2)

lst = [0, 1, 2, 3, 4]

# Slice the list to reverse it without using the .reverse() method
reversed_list = lst[::-1]
print("Reversed list:", reversed_list)
