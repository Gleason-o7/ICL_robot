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

user_idx = int(input("Enter index: "))


# Retrive index row
# Example: 6 // 4 = 1
row_val = user_idx // num_columns

# Retrive index column
# Example: 6 % 4 = 2
column_val = user_idx % num_columns


print(f"Row #{row_val}")
print(f"Column #{column_val}")

print(f"({row_val},{column_val})")

