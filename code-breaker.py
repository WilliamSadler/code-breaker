import numpy

original_message = ""
new_message = ""

encoding_table = [[" SZ", "ABC", "DEF"],["GHI", "JKL", "MNO"], ["PQR", "TUV", "WXY"]]

encryption_matrix = [[1, 0, 2], [1, 2, 0], [2, 1, 1]]

def get_table_vector(c):
    #Get 1x3 vector for specific character using the encoding table
    for i in range(0, len(encoding_table)):
        for j in range(0, len(encoding_table[i])):
            for n in range(0, len(encoding_table[i][j])):
                if encoding_table[i][j][n] == c:
                    return [i, j, n]

def from_table_vector(m):
    return encoding_table[m[0]][m[1]][m[2]]

def get_message(filepath):
    #Get message from text file (original_message.txt)
    f = open("original_message.txt")
    message_unformatted = f.read()

    return message_unformatted.strip().upper()

def matrix_multiply(K, m):
    #Function to multiple a 3x3 matrix (K) by a 3x1 matrix (m)
    return_array = []
    for i in range(0, len(K)):
        total = 0
        for j in range(0, len(K[i])):
            total = total + K[i][j]*m[j]
        print(str(K[i][j]) + " " + str(m[j]))
        return_array.append(total % 3)
        print(total)
        input()

    print(return_array)
    return return_array
       

if __name__ == "__main__":
    #Main function, this is where the code starts execution
    original_message = get_message("./original_message.txt")
    print(original_message)
    
    for char in original_message:
        s = get_table_vector(char)
        t = numpy.dot(encryption_matrix, s)
    
        for i in range(0, len(t)):
            t[i] = t[i] % 3

        print(t)
        c = from_table_vector(t)

        new_message = new_message + c

    print(new_message.replace(" ", "..."))

    