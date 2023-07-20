def codecor():
    def toggle_bit(bit):
        return 0 if bit == 1 else 1
    codeword = input("Enter the 21-bit codeword: ")
    part1 = codeword[:9]
    part2 = codeword[9:18]
    part3 = codeword[18:]
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
           
       rowf=0
       colf=0
    for i in range(3):
        if column_parity1[i]==1:
        colf=1
    for i in range(3):
        if row_parity1[i]==1:
        rowf=1
    if rowf!=0 and colf!=0 and rowf == colf:
        for i in range(3):
            for j in range(3):
                if row_parity1[i] == 1 and column_parity1[j] == 1:
                    matrix1[i][j] = toggle_bit(matrix1[i][j])
                    row_parity1[i] = 0;
                    column_parity1[j] = 0;
    elif rowf!=0 and colf!=0 and rowf != colf:
        for i in range(3):
            for j in range(3):
                if row_parity1[i] == 1 and column_parity1[j] == 1:
                matrix1[i][j] = toggle_bit(matrix1[i][j])
    else:
        for j in range(3):
            if column_parity1[j] == 1:
                matrix1[0][j] = toggle_bit(matrix1[0][j])

    print("Corrected Matrix 1:")
    for row in matrix1:
        print(row)
    
    rowf1=0
    colf1=0
    for i in range(3):
        if column_parity2[i]==1:
            colf1=1
    for i in range(3):
        if row_parity2[i]==1:
            rowf1=1
            
    if rowf1!=0 and colf1!=0 and rowf1 == colf1:
        for i in range(3):
            for j in range(3):
                if row_parity2[i] == 1 and column_parity2[j] == 1:
                    matrix2[i][j] = toggle_bit(matrix2[i][j])
                    row_parity2[i] = 0;
                    column_parity2[j] = 0;

    elif rowf1!=0 and colf1!=0 and rowf1 != colf1:
    for i in range(3):
        for j in range(3):
            if row_parity2[i] == 1 and column_parity2[j] == 1:
                matrix2[i][j] = toggle_bit(matrix2[i][j])

    else:
    for j in range(3):
        if column_parity2[j] == 1:
            matrix2[0][j] = toggle_bit(matrix2[0][j])

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

    rowf1=0
    colf1=0
    for i in range(3):
        if column_parity3[i]==1:
            colf1+=1
    for i in range(3):
        if row_parity3[i]==1:
            rowf1+=1
    if rowf1!=0 and colf1!=0 and rowf1 == colf1:
        for i in range(3):
            for j in range(3):
                if row_parity3[i] == 1 and column_parity3[j] == 1:
                    matrix3[i][j] = toggle_bit(matrix3[i][j])
                    row_parity3[i] = 0;
                    column_parity3[j] = 0;
    elif rowf1!=0 and colf1!=0 and rowf1 != colf1:
        for i in range(3):
            for j in range(3):
                if row_parity3[i] == 1 and column_parity3[j] == 1:
                    matrix3[i][j] = toggle_bit(matrix3[i][j])
                
    elif rowf1==1 and colf1==0:
        for i in range(3):
            if row_parity3[i] == 1:
                matrix3[i][0] = toggle_bit(matrix3[i][0])
    else:
        for j in range(3):
            if column_parity3[j] == 1:
                matrix3[0][j] = toggle_bit(matrix3[0][j])

    print("Corrected Matrix 3:")
    for row in matrix3:
        print(row)

    corrected_codeword = ''.join([''.join(map(str, row)) for row in matrix1 + matrix2 + [matrix3[2]]])
    print("Corrected 21-bit codeword:", corrected_codeword)




