'''
• Given the following formula for the Sørensen–Dice coefficient, create a python function that
calculates it: 
    
2|X ∩ Y| / |X| + |Y|
'''

def calculate_dice_coefficient(X, Y):
    intersection = len(set(X) & set(Y))
    union = len(set(X)) + len(set(Y))
    dice_coefficient = (2 * intersection) / union
    return dice_coefficient

X = [1, 2, 3, 4, 5, 6]
Y = [4, 5, 6, 7, 8, 9]

result = calculate_dice_coefficient(X, Y)
print("Sørensen–Dice coefficient:", result)
