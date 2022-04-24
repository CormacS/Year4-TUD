#Cormac Smith
#Some parts of this code was inspired by a tutorial online, was haing difficulties converting string to an appriopriate matrix. The rest is just maths.

import sys
import numpy as np


ans = input("1 to Encrypt\n2 to Decrypt\n")

if(ans == "1"):
    msg = input("Enter message to encrypt: ").upper()
    msg = msg.replace(" ", "")

    #turns word into a matrix
    row = 2
    col = int(len(msg)/2)
    msgMatrix = np.zeros((row, col), dtype=int)

    counter1 = 0
    counter2 = 0

    #Getting the ord will give the unicode value of that letter, minus 65 to get its value(which will be added back later)
    for i in range(len(msg)):
        if i % 2 == 0:
            msgMatrix[0][counter1] = int(ord(msg[i])-65)
            counter1 += 1
        else:
            msgMatrix[1][counter2] = int(ord(msg[i])-65)
            counter2 += 1

    key = input("Enter 4 letter key: ").upper()
    key = key.replace(" ", "")

    #np.zero makes a 2 by 2 Matrix
    keyMatrix = np.zeros((2, 2), dtype=int)
    counter3 = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[counter3])-65
            counter3 += 1

    # finding determinant
    deter = keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]
    deter = deter % 26

    # finding multiplicative inverse
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue

    if mul_inv == -1:
        print("Invalid key")
        sys.exit()


    encryp_text = ""
    itr_count = int(len(msg)/2)

    #adding 65 will give the unicode for the letter
    for i in range(itr_count):
        temp1 = msgMatrix[0][i] * keyMatrix[0][0] + msgMatrix[1][i] * keyMatrix[0][1]
        encryp_text += chr((temp1 % 26) + 65)
        temp2 = msgMatrix[0][i] * keyMatrix[1][0] + msgMatrix[1][i] * keyMatrix[1][1]
        encryp_text += chr((temp2 % 26) + 65)

    print("Encrypted Text: "+ encryp_text)


if(ans == "2"):
    msg = input("Enter encrypted message to decrypt: ").upper()
    msg = msg.replace(" ", "")

    row = 2
    col = int(len(msg) / 2)
    msgMatrix = np.zeros((row, col), dtype=int)

    counter1 = 0
    counter2 = 0
    #turn characters into numbers with unicode ord function
    for i in range(len(msg)):
        if i % 2 == 0:
            msgMatrix[0][counter1] = int(ord(msg[i]) - 65)
            counter1 += 1
        else:
            msgMatrix[1][counter2] = int(ord(msg[i]) - 65)
            counter2 += 1

    key = input("Enter 4 letter key: ").upper()
    key = key.replace(" ", "")

    #create a 2 by 2 matrix
    keyMatrix = np.zeros((2, 2), dtype=int)
    counter3 = 0
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = ord(key[counter3]) - 65
            counter3 += 1

    #finding determinent
    deter = keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[0][1] * keyMatrix[1][0]
    deter = deter % 26

    #finding multiplicative inverse
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue

    keyMatrix[0][0], keyMatrix[1][1] = keyMatrix[1][1], keyMatrix[0][0]

    #Adjugate Matrix
    keyMatrix[0][1] *= -1
    keyMatrix[1][0] *= -1

    keyMatrix[0][1] = keyMatrix[0][1] % 26
    keyMatrix[1][0] = keyMatrix[1][0] % 26

    #Multiply the multicplicative inverse by adjugate matrix
    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] *= mul_inv

    for i in range(2):
        for j in range(2):
            keyMatrix[i][j] = keyMatrix[i][j] % 26

    #Add 65 to the number to bring it in unicode using chr
    decryp_text = ""
    itr_count = int(len(msg) / 2)
    for i in range(itr_count):
        temp1 = msgMatrix[0][i] * keyMatrix[0][0] + msgMatrix[1][i] * keyMatrix[0][1]
        decryp_text += chr((temp1 % 26) + 65)
        temp2 = msgMatrix[0][i] * keyMatrix[1][0] + msgMatrix[1][i] * keyMatrix[1][1]
        decryp_text += chr((temp2 % 26) + 65)


    print("Decrypted Text: "+ decryp_text)
