morsecodedictionary = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

def ENCRYPTION(text):
    enc = ''
    for each in text:
        if each != ' ':
            enc += morsecodedictionary[each] + ' '
        else:
            enc += ' '
    return enc

def DECRYPTION(text):
    text += ' '
    dec = ''
    citext = ''
    k = 0

    for each in text:
        if each != ' ':
            k = 0
            citext += each
        else:
            k += 1
            if k == 2:
                dec += ' '
            else:
                if citext in morsecodedictionary.values():
                    dec += list(morsecodedictionary.keys())[
                        list(morsecodedictionary.values()).index(citext)
                    ]
                citext = ''
    return dec

# Driver Code
print("Enter Text: ")
Info = input()
result = ENCRYPTION(Info.upper())
print("Encrypted:", result)

Info = result
result = DECRYPTION(Info)
print("Decrypted:", result)
