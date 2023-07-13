'''
Print the following pattern
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

for i in range(1, 6):  # outer loop for rows
    for j in range(1, i + 1):  # inner loop for columns
        print(j, end=" ")
    print()
