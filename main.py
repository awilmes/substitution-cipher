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

    Args:
        natural_alphabet (str): An uppercase string of the natrual alphabet.

    Returns:
        str: A 26 character string key.
    '''
    # Concatenate a string with samples taken from the natural alphabet until reaching the length of the natural alphabet.
    return ''.join(random.sample(natural_alphabet, len(natural_alphabet)))


def encrypt(natural_alphabet, plaintext, key):
    '''
    Encryption method. Takes plaintext and a key as arguments. Converts each plaintext
    character to an index number, and matches the index number against the key.

    Args:
        natural_alphabet (str): An uppercase string of the natrual alphabet.
        plaintext (str): User input to be cleaned.
        key (str): An uppercase string of a permutated alphabet.

    Returns:
        str: A string of ciphertext.
    '''
    PLAINTEXT = clean_plaintext(natural_alphabet, plaintext) # Clean the plaintext on declaration.

    # Create an empty array to hold index numbers of plaintext characters:
    natural_index_nums = []

    # Convert plaintext characters to index numbers based on the natural alphabet:
    for char in PLAINTEXT:
        natural_index_nums.append(get_char_index(natural_alphabet, char))

    # Create an empty array to hold ciphertext characters as they are discovered:
    ciphertext_array = []

    # Convert index numbers to characters based on the permutated alphabet and 
    # store in an array:
    for index in natural_index_nums:
        ciphertext_array.append(convert_index_to_char(key, index))

    # Return a string version of the ciphertext array:    
    return ''.join(ciphertext_array)


def decrypt(natural_alphabet, ciphertext, key):
    '''
    Decryption method. Takes ciphertext and a key as arguments. Works the same as the
    encryption method but in reverse. 
    
    Args:
        natural_alphabet (str): An uppercase string of the natrual alphabet.
        ciphertext (str): A string of ciphertext to be decrypted.
        key (str): An uppercase string of a permutated alphabet.
        
    Returns:
        str: A string of decrypted ciphertext.
    '''
    # Create an empty array to store index numbers:
    permutated_index_nums = []

    # Convert the ciphertext characters to index numbers:
    for char in ciphertext:
        permutated_index_nums.append(get_char_index(key, char))

    # Create an empty array to hold characters as they are decrypted:
    plaintext_array = []

    # Convert the index array to natural characters and store in an array:
    for index in permutated_index_nums:
        plaintext_array.append(convert_index_to_char(natural_alphabet, index))

    # Return a string version of the plaintext array:
    return ''.join(plaintext_array)



def clean_plaintext(natural_alphabet, plaintext):
    '''
    Cleans plaintext by converting to uppercase, removing whitespace, and 
    removing special characters. Ignores any character not in the natural
    alphabet.

    Args:
        natural_alphabet (str): An uppercase string of the natrual alphabet.
        plaintext (str): User input to be cleaned.
    
    Returns:
         str: A string of cleaned plaintext.
    '''
    # Convert the text to uppercase:
    upper_plaintext = plaintext.upper()

    # Declare an empty array to hold valid characters:
    valid_chars = []

    # Loop through each character in PLAINTEXT, adding it to valid_chars found
    # in natural_alphabet:
    for char in upper_plaintext:
        if not char in natural_alphabet:
            continue
        else:
            valid_chars.append(char)

    # Return the cleaned plaintext:
    return ''.join(valid_chars)


def get_char_index(string, char):
    '''
    Gets the index of a character in a given string.

    Args:
        string (str): A string containing an alphabet or key.
        char (str): The character to return the index value of.
    
    Returns:
        int: An integer of the character's index value.
    '''
    index = string.index(char)
    return index


def convert_index_to_char(string, index):
    '''
    Gets the character of a provided index value from a given string.

    Args:
        string (str): A string of the alphabet or key being searched.
        index (int): The index value of the character being matched.

    Returns:
        str: The string character that matches the index value.
    '''
    char = string[index]
    return char


def main():
    '''
    Simple method that demonstrates program functionality.
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
    PLAINTEXT = input('Enter plaintext: ')
    print(f'\nPlaintext : {PLAINTEXT}')

    # Encrypt the plaintext
    CIPHERTEXT = encrypt(natural_alphabet, PLAINTEXT, key)
    print(f'Ciphertext: {CIPHERTEXT}\n')

    # Decrypt the ciphertext
    DECRYPTED_TEXT = decrypt(natural_alphabet, CIPHERTEXT, key)
    print(f'Decrypted Ciphertext: {DECRYPTED_TEXT}\n')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()