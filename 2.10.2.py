#2d table
# ask for numrows, numcolumns, gen table, get row/column index and output va

#Get user input defining table bounds
num_rows = int(input("Enter the number of rows: "))
num_columns = int(input("Enter the number of coluns: "))

# generate table based on size
# note: table will be filled, so values need not be initialized


# Original for loop run:
'''
accumulator = 0
for i in range(num_columns):
    for j in range(num_rows):
        table[i][j] = accumulator
        accumulator += 1
'''

# cooler for loop initializer
table = [[(i * num_columns + j) for j in range(num_columns)] for i in range(num_rows)]

user_row = int(input("Enter row index: "))
user_column = int(input("Enter column index: "))

print(table[user_row - 1][user_column - 1])

input("Show entire table?")

for row in table:
    print(row)

