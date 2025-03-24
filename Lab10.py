import time

try:
    import board
    import neopixel
    CPX_MODE = True  
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.3)
except ImportError:
    CPX_MODE = False  

MORSE_CODE = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
    'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
    'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
    'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def clean_text(text):
    text = text.lower()
    return ''.join(char for char in text if char in MORSE_CODE)

def text_to_morse(text):
    morse_code = []
    words = text.split()  

    for word in words:
        letters = [MORSE_CODE[char] for char in word]  
        morse_code.append(' '.join(letters)) 

    return ' // '.join(morse_code)  

def display_morse_on_cpx(morse_code, unit_time, color):
    for symbol in morse_code:
        if symbol == '.':
            light_up(color, unit_time)  
        elif symbol == '-':
            light_up(color, unit_time * 3)  
        elif symbol == ' ':
            time.sleep(unit_time)  
        elif symbol == '/':
            time.sleep(unit_time * 7)  

def light_up(color, duration):
    pixels.fill(color)
    time.sleep(duration)
    pixels.fill((0, 0, 0))
    time.sleep(duration)

def main():
    try:
        unit_time = float(input("Enter unit time (0-1s): "))
        user_input = input("Enter a sentence: ")
        cleaned_text = clean_text(user_input)
        morse_code = text_to_morse(cleaned_text)
        print(f"Morse Code: {morse_code}")

        if CPX_MODE:
            color = (0, 255, 0)
            display_morse_on_cpx(morse_code, unit_time, color)
    except ValueError:
        print("Error: Enter a valid number for unit time.")

if __name__ == "__main__":
    main()