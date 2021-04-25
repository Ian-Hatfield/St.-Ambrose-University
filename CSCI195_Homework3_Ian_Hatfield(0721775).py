# Ian Hatfield
# CSCI195_Homework3_Ian_Hatfield(0721775)

# Q1: Declare two string variable, join them together
# and print the result

name = 'Winston'
name_two = 'Sir '
print("Hello " + name_two + name)

# Q2: Use a for loop to print all the characters in a string
# (one character in one iteraration)

name = 'kyle'
for i in range(len(name)):
    print(name[i])

# Q3: Declare one string that consists of at least 10 characters,
# then print the first character, print the last character, print
# the 6th character, print from the first to the 4th characters,
# print from the second to the second to last

name = 'Washington'
print(name[0])
print(name[-1])
print(name[5])
print(name[0:3])
print(name[1:-2])

# Q4: Add your code to the CaesarEncrypt() function in the slides
# to deal with the upper case letters ('A'<=ch<='Z'), and define
# the CaesarDecrypt(cypherText, n) function to return the plainText
# Note You also need to write some test code for functions in Q4

def CaesarEncrypt(plainText, n):

    cipherText = ''

    for ch in plainText:
        if 'a'<=ch<='z':
            index = ord(ch) - ord('a')
            index = (index + n) % 26
            new_ch = chr(index + ord('a'))
        elif 'A'<=ch<='Z':
            ...  # add your code here to replace pass
        else:
            new_ch = ch

        cipherText = cipherText + new_ch
    return cipherText


def CaesarDecrypt(cipherText, n):
    plainText = ''

    for ch in plainText:
        if 'a'<=ch<='z':
            index = ord(ch) - ord('a')
            index = (index - n) % 26
            new_ch = chr(index + ord('a'))
        elif 'A'<=ch<='Z':
            ...  # add your code here to replace pass
        else:
            new_ch = ch

        plainText = plainText + new_ch
    return plainText

plainText = "Washington"
n = 5
cipherText = CaesarEncrypt(plainText, n)
print(cipherText)

plainText = CaesarDecrypt(cipherText, n)
print(plainText)
