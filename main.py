#!/usr/bin/env python3
'''
Programmer: Andrew Wilmes
Date: 17 May 2023
Desc: Substitution Cipher
'''
import random


# Declare a constant array of the natural alphabet:
CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate_key():
    '''
    Generate an alphabet permutation to serve as a key.
    Returns a 26 character array.
    '''
    # Create an empty array to hold the generated key:
    permutation_array = []    
    '''
    Pick a random character from the CHARS array. If the random character is not 
    in the CHARS_OUT array, add it to the CHARS_OUT array. Loop until the CHARS_OUT 
    array length is equal to 26.
    '''
    while len(permutation_array) < 26:
        char = random.choice(CHARS)
        if not char in permutation_array:
            permutation_array.append(char)

    # Return the generated key array:
    return permutation_array


def encrypt(plaintext, key):
    '''
    Encryption method. Takes plaintext and a key as arguments. Converts each plaintext
    character to an index number, and matches the index number against the key.
    Returns ciphertext string.
    '''
    KEY = key
    PLAINTEXT = clean_plaintext(plaintext) # Clean the plaintext on declaration.

    # Create an empty array to hold index numbers of plaintext characters:
    natural_index_nums = []

    # Convert plaintext characters to index numbers based on the natural alphabet:
    for char in PLAINTEXT:
        natural_index_nums.append(get_character_index(CHARS, char))

    # Create an empty array to hold ciphertext characters as they are discovered:
    ciphertext_array = []

    # Convert index numbers to characters based on the permutated alphabet:
    for index in natural_index_nums:
        ciphertext_array.append(convert_index_to_character(KEY, index))

    # Convert the ciphertext array to a string and return it:
    ciphertext_string = ""
    for char in ciphertext_array:
        ciphertext_string += char
    
    return ciphertext_string


def decrypt(ciphertext, key):
    '''
    Decryption method. Takes ciphertext and a key as arguments. Works the same as the
    encryption method but in reverse. Returns a string of decrypted ciphertext.
    '''
    CIPHERTEXT = ciphertext
    KEY = key

    # Create an empty array to store index numbers:
    permutated_index_nums = []

    # Convert the ciphertext characters to index numbers:
    for char in CIPHERTEXT:
        permutated_index_nums.append(get_character_index(KEY, char))

    # Create an empty array to hold characters as they are decrypted:
    plaintext_array = []

    # Convert the index array to natural characters:
    for index in permutated_index_nums:
        plaintext_array.append(convert_index_to_character(CHARS, index))

    # Convert the plaintext array back to a string:
    plaintext_string = ""
    for char in plaintext_array:
        plaintext_string += char

    return plaintext_string



def clean_plaintext(plaintext):
    '''
    Cleans plaintext by converting to uppercase, removing
    whitespace, and removing special characters. Returns
    an array.
    '''
    # Convert the text to uppercase:
    PLAINTEXT = plaintext.upper()

    # Declare an empty array to hold clean plaintext:
    clean_plaintext = []

    # Loop through each character in PLAINTEXT, adding it
    # to clean_text if it is valid:
    for char in PLAINTEXT:
        if not char in CHARS:
            continue
        else:
            clean_plaintext.append(char)

    # Return the cleaned plaintext:
    return clean_plaintext


def get_character_index(array, char):
    '''
    Returns the index of a character in a given array.
    '''
    index = array.index(char)
    return index


def convert_index_to_character(array, index):
    '''
    Returns the ciphertext character of a given index.
    '''
    cipher_char = array[index]
    return cipher_char


def test_main():
    '''
    Test method that verifies program functionality.
    '''
    print('\nSIMPLE SUBSTITUTION CIPHER\nAndrew Wilmes 2023\n')

    # Generate a key for encrypting/decrypting:
    KEY = generate_key()
    print(f'Natural Alphabet   : {CHARS}')
    print(f'Permutated Alphabet: {KEY}\n')

    # Get plaintext from the user
    PLAINTEXT = input("Enter plaintext: ")
    print(f'\nPlaintext : {PLAINTEXT}')

    # Encrypt the plaintext
    CIPHERTEXT = encrypt(PLAINTEXT, KEY)
    print(f'Ciphertext: {CIPHERTEXT}\n')

    # Decrypt the ciphertext
    DECRYPTED_TEXT = decrypt(CIPHERTEXT, KEY)
    print(f'Decrypted Ciphertext: {DECRYPTED_TEXT}\n')


def main():
    '''
    Main method.
    '''
    # TODO: Add args to allow the user to output key to a file, load keys, load text files, etc.
    pass


if __name__ == "__main__":
    test_main()
    # main()
