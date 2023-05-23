#!/usr/bin/env python3
'''
Contains space for snippets and tool development.
'''


def analyze_ciphertext(ciphertext):
    '''
    Analyze a string of ciphertext to determine the number of occurences for each character.

        Args:
            ciphertext (str): The string of ciphertext to be analyzed.

        Returns:
            List (str): Counts of character occurences.
    '''
    # INPUT: GSVPVBGLGSVXLEVI
    # Create a temporary dict to hold key/value pairs:
    temp_dict = {} # Note: Using a dict will automatically remove duplicates
    
    # Loop through each ciphertext character, adding the character and
    # its count to the temp dict
    for i in ciphertext:
        temp_dict[i] = ciphertext.count(i)

    # Create a list to hold key/value pairs:
    output_list = []
    
    # Convert the temp dict to a list:
    for key, value in temp_dict.items():
        output_list.append((key, value))

    return output_list


def add_frequency(list, divisor):
    '''
    Adds a frequency weight value to a list of key/value pairs.

        Args:
            list (str, int): A string containing key/values of characters and their occurences.
            divisor (int): The number to divide by representing the total length of the ciphertext.

        Returns:
            List (str, int, float): A list of items with each containing information on a character, its
                number of occurences, and a frequency weight.
    '''
    # Create an empty list to store output
    output_list = []
    
    # Loop through input list, calculating frequency and storing values in the output list:
    # Frequency formula: frequency = (character_count / ciphertext_length) * 100
    for i in list:
        output_list.append((i[0], i[1], float((i[1] / divisor) * 100)))

    return output_list


def main():
    
    LETTER_FREQUENCY_DICT = {
        'E': 12.02,
        'T': 9.10,
        'A': 8.12,
        'O': 7.68,
        'I': 7.31,
        'N': 6.95,
        'S': 6.28,
        'R': 6.02,
        'H': 5.92,
        'D': 4.32,
        'L': 3.98,
        'U': 2.88,
        'C': 2.71,
        'M': 2.61,
        'F': 2.30,
        'Y': 2.11,
        'W': 2.09,
        'G': 2.03,
        'P': 1.82,
        'B': 1.49,
        'V': 1.11,
        'K': 0.69,
        'X': 0.17,
        'Q': 0.11,
        'J': 0.10,
        'Z': 0.07
    }

    ciphertext = 'GSVPVBGLGSVXLEVI'
    # Get a list of characters with their counts:
    list_of_counts = analyze_ciphertext(ciphertext)
    # Sort the list of character counts by value from largest to smallest:
    list_of_counts = sorted(list_of_counts, key=lambda x: x[1], reverse=True)
    # Add a third value of frequency to each list element:
    list_of_counts_and_frequencies = add_frequency(list_of_counts, len(ciphertext))

    header = ['CHAR', 'COUNT', 'FREQ']
    print(f'{header[0]:-^12}{header[1]:-^12}{header[2]:-^12}')
    for i in list_of_counts_and_frequencies:
        print(f'{i[0]:^12}{i[1]:^12}{i[2]:^12}')

    # print('CHAR  FREQ')
    # for k, v in sorted(char_frequency.items(), ):
    #     print(f'  {k}    {v}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
