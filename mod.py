#!/usr/bin/env python3
'''
Contains space for snippets and tool development.
'''


def cipher_analysis(ciphertext):
    '''
    A simple function to analyze a string of ciphertext.

        Args:
            ciphertext (str): The string of ciphertext to be analyzed.

        Returns:
            str: Letter frequency.
    '''
    # INPUT: GSVPVBGLGSVXLEVI
    # Create a dictionary to hold values:
    output = {}
    for i in ciphertext:
        output[i] = ciphertext.count(i)

    return output


def get_frequency(dict, divisor):
    output = {}
    
    for k, v in dict.items():
        output[k] = float((v / divisor) * 100)

    return output



def main():
    LETTER_FREQUENCY = {
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
    output = cipher_analysis(ciphertext)
    char_frequency = get_frequency(output, len(ciphertext))


    print('CHAR  FREQ')
    for k, v in char_frequency.items():
        print(f'  {k}    {v}')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
