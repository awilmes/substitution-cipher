#!/usr/bin/env python3
'''
Programmer: Andrew Wilmes
Date: 17 May 2023
Desc: Substitution Cipher
'''
import random


def generate_key(natural_alphabet):
    '''
    Generate an alphabet permutation to serve as a key.
    Returns a 26 character array.
    '''
    # Create an empty array to hold the generated key:
    permutated_alphabet = ''    
    '''
    Pick a random character from the CHARS array. If the random character is not 
    in the CHARS_OUT array, add it to the CHARS_OUT array. Loop until the CHARS_OUT 
    array length is equal to 26.
    '''
    while len(permutated_alphabet) < 26:
        char = random.choice(natural_alphabet)
        if not char in permutated_alphabet:
            permutated_alphabet += char

    # Return the generated key array:
    return permutated_alphabet


def encrypt(natural_alphabet, plaintext, key):
    '''
    Encryption method. Takes plaintext and a key as arguments. Converts each plaintext
    character to an index number, and matches the index number against the key.
    Returns ciphertext string.
    '''
    PLAINTEXT = clean_plaintext(natural_alphabet, plaintext) # Clean the plaintext on declaration.

    # Create an empty array to hold index numbers of plaintext characters:
    natural_index_nums = []

    # Convert plaintext characters to index numbers based on the natural alphabet:
    for char in PLAINTEXT:
        natural_index_nums.append(get_character_index(natural_alphabet, char))

    # Create an empty array to hold ciphertext characters as they are discovered:
    ciphertext_array = []

    # Convert index numbers to characters based on the permutated alphabet:
    for index in natural_index_nums:
        ciphertext_array.append(convert_index_to_character(key, index))

    # Convert the ciphertext array to a string and return it:
    ciphertext_string = ""
    for char in ciphertext_array:
        ciphertext_string += char
    
    return ciphertext_string


def decrypt(natural_alphabet, ciphertext, key):
    '''
    Decryption method. Takes ciphertext and a key as arguments. Works the same as the
    encryption method but in reverse. Returns a string of decrypted ciphertext.
    '''
    # Create an empty array to store index numbers:
    permutated_index_nums = []

    # Convert the ciphertext characters to index numbers:
    for char in ciphertext:
        permutated_index_nums.append(get_character_index(key, char))

    # Create an empty array to hold characters as they are decrypted:
    plaintext_array = []

    # Convert the index array to natural characters:
    for index in permutated_index_nums:
        plaintext_array.append(convert_index_to_character(natural_alphabet, index))

    # Convert the plaintext array back to a string:
    plaintext_string = ""
    for char in plaintext_array:
        plaintext_string += char

    return plaintext_string



def clean_plaintext(natural_alphabet, plaintext):
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
        if not char in natural_alphabet:
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

    # Declare a string constant of the natural alphabet:
    natural_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Generate a key for encrypting/decrypting:
    key = generate_key(natural_alphabet)

    # Display natural and permutated alphabets:
    print(f'Natural Alphabet   : {natural_alphabet}')
    print(f'Permutated Alphabet: {key}\n')

    # Get plaintext from the user
    PLAINTEXT = input("Enter plaintext: ")
    print(f'\nPlaintext : {PLAINTEXT}')

    # Encrypt the plaintext
    CIPHERTEXT = encrypt(natural_alphabet, PLAINTEXT, key)
    print(f'Ciphertext: {CIPHERTEXT}\n')

    # Decrypt the ciphertext
    DECRYPTED_TEXT = decrypt(natural_alphabet, CIPHERTEXT, key)
    print(f'Decrypted Ciphertext: {DECRYPTED_TEXT}\n')


def main():
    '''
    Main method.
    '''
    # TODO: Add args to allow the user to output key to a file, load keys, load text files, etc.
    pass


if __name__ == "__main__":
    try:
        test_main()
        # main()
    except KeyboardInterrupt:
        exit()