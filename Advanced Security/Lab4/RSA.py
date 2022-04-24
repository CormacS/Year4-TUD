counter = False
counter2 = False

#Get Primse numbers
while counter != True or counter2 != True:
    prime = int(input("Enter 1st prime number: "))
    prime2 = int(input("Enter 2nd prime number: "))

    if prime > 1:
        for i in range (2,prime):
            if (prime % i) == 0:
                print(prime, " is not a prime number, please do again")
                break
        else:   
            print(prime," is Prime")
            counter = True
    
    if prime2 > 1:
        for i in range (2,prime2):
            if (prime2 % i) == 0:
                print(prime2, " is not a prime number, please do again")
                break
        else:   
            print(prime2, "is Prime")
            counter2 = True

#Calculate n, e and phi
n = prime * prime2
phi = (prime-1) * (prime2-1)
e = 17

#Calculate greatest common divisor

def getPrivateKey():
    phi
    e

    def euclid(num1, num2, num3, num4):
        if num3 == 1:
            key = num4
            return key
        else:
            newNum3 = num1 - ((num1 // num3) * num3)
            newNum4 = (num2 - (num4 * (num1 // num3))) % phi
            return euclid(num3, num4, newNum3, newNum4)

    return euclid(phi, phi, e, 1)

privateKey = getPrivateKey()


sentence = input("What is the sentence you want to encrypt: ")


#Encrypt their message using ord, e and n
encrypted = []

for letter in sentence:
    ltr = (ord(letter) ** e ) % n
    encrypted.append(ltr)


print("Message to encrypt: ",sentence)
print("Private Key: ",privateKey)
print("Msg when encrypted is : ",encrypted)

#Decrypt using the key, char and n

d = int(input("What is your private key: "))
if d == privateKey:
    decrypt = []
    for letter in encrypted:
        ltr = chr((letter**d) % n)
        decrypt.append(ltr)

print("Decrpyted: ",''.join(decrypt))