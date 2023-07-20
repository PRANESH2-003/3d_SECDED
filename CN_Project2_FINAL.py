binary_numbers = input("Enter a binary number: ")

# Check if the binary number has less than 8 digits
if len(binary_numbers) < 8:
    binary_numbers = '0' * (8 - len(binary_numbers)) + binary_numbers

print("Modified binary number:", binary_numbers)
    
# Split the binary numbers into two halves
first_half = binary_numbers[:4]
second_half = binary_numbers[4:]

# Split each half into two halves
first_half_parts = [first_half[i:i+2] for i in range(0, len(first_half), 2)]
second_half_parts = [second_half[i:i+2] for i in range(0, len(second_half), 2)]

# Create Matrix 1 along with parity
matrix1 = []
row_parity1 = []
for i in range(len(first_half_parts)):
    row_data = [int(bit) for bit in first_half_parts[i]]
    row_parity = 1 if sum(row_data) % 2 == 1 else 0  # Generate parity for row
    row_data.append(row_parity)
    matrix1.append(row_data)
    row_parity1.append(row_parity)

# Calculate Column Parity for Matrix 1
column_parity1 = []
for j in range(len(matrix1[0])):
    column_data = [row[j] for row in matrix1]
    column_parity = 1 if sum(column_data) % 2 == 1 else 0  # Generate parity for column
    column_parity1.append(column_parity)

matrix1.append(column_parity1)

# Create Matrix 2 along with parity
matrix2 = []
row_parity2 = []
for i in range(len(second_half_parts)):
    row_data = [int(bit) for bit in second_half_parts[i]]
    row_parity = 1 if sum(row_data) % 2 == 1 else 0  # Generate parity for row
    row_data.append(row_parity)
    matrix2.append(row_data)
    row_parity2.append(row_parity)

# Calculate Column Parity for Matrix 2
column_parity2 = []
for j in range(len(matrix2[0])):
    column_data = [row[j] for row in matrix2]
    column_parity = 1 if sum(column_data) % 2 == 1 else 0  # Generate parity for column
    column_parity2.append(column_parity)

matrix2.append(column_parity2)

# Calculate Column Parity for the last row of both matrices
last_row_matrix1 = [row[-1] for row in matrix1[:-1]]
last_row_matrix2 = [row[-1] for row in matrix2[:-1]]
column_parity_last_row = []

max_length = max(len(last_row_matrix1), len(last_row_matrix2))
for j in range(max_length):
    column_data = [last_row_matrix1[j] if j < len(last_row_matrix1) else 0,
                   last_row_matrix2[j] if j < len(last_row_matrix2) else 0]
    column_parity = 1 if sum(column_data) % 2 == 1 else 0  # Generate parity for column
    column_parity_last_row.append(column_parity)

# Generate parity for the obtained row parities
row_parity_data = last_row_matrix1 + last_row_matrix2
row_parity = 1 if sum(row_parity_data) % 2 == 1 else 0  # Generate parity for row parities
column_parity_last_row.append(row_parity)

# Create the column parity matrix for the last row
column_parity_matrix = [column_parity_last_row]

# Print Matrix 1 along with parity
print("Matrix 1 along with parity:")
for row in matrix1:
    print(row)

# Print Matrix 2 along with parity
print("Matrix 2 along with parity:")
for row in matrix2:
    print(row)

# Print the Column Parity Matrix for the last row
print("Column Parity Matrix for Last Row:")
for row in column_parity_matrix:
    print(row)

codeword = ""
matrices = [matrix1, matrix2, column_parity_matrix]

for matrix in matrices:
    for row in matrix:
        codeword += "".join(map(str, row))

print("Codeword:", codeword)

def toggle_bit(bit):
    return 0 if bit == 1 else 1

# Divide the codeword into 3 parts: 9-bit, 9-bit, and 3-bit
part1 = codeword[:9]
part2 = codeword[9:18]
part3 = codeword[18:]

# Convert each part into a 3x3 matrix (Matrix 1)
matrix1 = [[int(bit) for bit in part1[i:i+3]] for i in range(0, 9, 3)]
matrix2 = [[int(bit) for bit in part2[i:i+3]] for i in range(0, 9, 3)]

# Calculate row parity for Matrix 1
row_parity1 = [sum(row) % 2 for row in matrix1]
row_parity2 = [sum(row) % 2 for row in matrix2]


# Calculate column parity for Matrix 1
column_parity1 = [sum(column) % 2 for column in zip(*matrix1)]
column_parity2 = [sum(column) % 2 for column in zip(*matrix2)]


# Print the original Matrix 1 along with row and column parities
print("Original Matrix 1:")
for row in matrix1:
    print(row)
print("Row Parity for Matrix 1:", row_parity1)
print("Column Parity for Matrix 1:", column_parity1)

print("Original Matrix 2:")
for row in matrix2:
    print(row)
print("Row Parity for Matrix 2:", row_parity2)
print("Column Parity for Matrix 2:", column_parity2)

# Correct errors in Matrix 1 based on row and column parities
rowf=0
colf=0
for i in range(3):
    if column_parity1[i]==1:
        colf=1
for i in range(3):
    if row_parity1[i]==1:
        rowf=1
if rowf==1 and colf==1:
    for i in range(3):
        for j in range(3):
            if row_parity1[i] == 1 and column_parity1[j] == 1:
                matrix1[i][j] = toggle_bit(matrix1[i][j])
                row_parity1[i] = 0
                column_parity1[j] = 0
elif rowf==1 and colf==0:
    for i in range(3):
        if row_parity1[i] == 1:
            matrix1[i][0] = toggle_bit(matrix1[i][0])
            row_parity1[i] = 0
else:
    for j in range(3):
        if column_parity1[j] == 1:
            matrix1[0][j] = toggle_bit(matrix1[0][j])
            column_parity1[j] = 0

# Print the corrected Matrix 1
print("Corrected Matrix 1:")
for row in matrix1:
    print(row)
    
# corrected Matrix 2
rowf1=0
colf1=0
for i in range(3):
    if column_parity2[i]==1:
        colf1=1
for i in range(3):
    if row_parity2[i]==1:
        rowf1=1
if rowf1==1 and colf1==1:
    for i in range(3):
        for j in range(3):
            if row_parity2[i] == 1 and column_parity2[j] == 1:
                matrix2[i][j] = toggle_bit(matrix2[i][j])
                row_parity2[i] = 0
                column_parity2[j] = 0
elif rowf1==1 and colf1==0:
    for i in range(3):
        if row_parity2[i] == 1:
            matrix2[i][0] = toggle_bit(matrix2[i][0])
            row_parity2[i] = 0
else:
    for j in range(3):
        if column_parity2[j] == 1:
            matrix2[0][j] = toggle_bit(matrix2[0][j])
            column_parity2[j] = 0

# Print the corrected Matrix 2
print("Corrected Matrix 2:")
for row in matrix2:
    print(row)

# Generate matrix3 based on the specified rows and last part of the codeword
matrix3 = [matrix1[-1]]  # First row
matrix3.append(matrix2[-1])  # Second row
matrix3.append([int(bit) for bit in part3])# Third row

# Print Matrix 3
print("Original Matrix 3:")
for row in matrix3:
    print(row)
#parity generation for matrix 3
row_parity3 = [sum(row) % 2 for row in matrix3]
column_parity3 = [sum(column) % 2 for column in zip(*matrix3)]
print("Row Parity for Matrix 1:", row_parity1)
print("Column Parity for Matrix 1:", column_parity1)

    
# corrected Matrix 3
rowf1=0
colf1=0
for i in range(3):
    if column_parity3[i]==1:
        colf1=1
for i in range(3):
    if row_parity3[i]==1:
        rowf1=1
if rowf1==1 and colf1==1:
    for i in range(3):
        for j in range(3):
            if row_parity3[i] == 1 and column_parity3[j] == 1:
                matrix3[i][j] = toggle_bit(matrix3[i][j])
                row_parity3[i] = 0
                column_parity3[j] = 0
elif rowf1==1 and colf1==0:
    for i in range(3):
        if row_parity3[i] == 1:
            matrix3[i][0] = toggle_bit(matrix3[i][0])
            row_parity3[i] = 0
else:
    for j in range(3):
        if column_parity3[j] == 1:
            matrix3[0][j] = toggle_bit(matrix3[0][j])
            column_parity3[j] = 0

# Print the corrected Matrix 3
print("Corrected Matrix 3:")
for row in matrix3:
    print(row)

corrected_codeword = ''.join([''.join(map(str, row)) for row in matrix1 + matrix2 + [matrix3[2]]])

print("Corrected 21-bit codeword:", corrected_codeword)
