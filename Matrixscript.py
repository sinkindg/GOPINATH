def decode_matrix(rows, columns, matrix):
    decoded_script = ''
    for j in range(columns):
        for i in range(rows):
            char = matrix[i][j]
            if char.isalnum():
                decoded_script += char
            elif decoded_script and decoded_script[-1] != ' ':
                decoded_script += ' '
    return decoded_script

# Sample input
rows, columns = 7, 3
matrix = [
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "ir!"
]

# Decode the matrix script
decoded_script = decode_matrix(rows, columns, matrix)

# Replace symbols or spaces between alphanumeric characters with a single space
decoded_script = decoded_script.replace('  ', ' ')

# Print the decoded script
print(decoded_script)
