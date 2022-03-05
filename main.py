MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----',
                    ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', "'": ".----.",
                    '"': '.-..-.', '_': '..--.-', ':': '---...',
                    ';': '-.-.-.', '!': '-.-.--', '+': '.-.-.',
                    '=': '-...-', '@': '.--.-.', ' ': '.......',
                    'Ą': '.-.-', 'Ć': '-.-..', 'Ę': '..-..',
                    'Ł': '.-..-', 'Ń': '--.--', 'Ó': '---.',
                    'Ś': '...-...', 'Ż': '--.-.', 'Ź': '--.-',
                    }


def to_morse(text):
    morse_code = []
    for letter in text:
        temp = letter.upper()
        morse_code.append(MORSE_CODE_DICT[temp])

    return morse_code


# def to_polish(text):
#     message = ""
#     for item in text:
#         message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(item)]
#
#     return message


text = input("Podaj wiadomość do zakodowania: ")
coded = to_morse(text=text)
for letter in coded:
    print(letter)




