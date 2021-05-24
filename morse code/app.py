from playsound import playsound
import time 
import argparse
import pyttsx3 as pyttsx 
from flask import Flask, render_template, request


app = Flask(__name__)
MORSE_CODE_DICT = { ' ':'/', 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}

def txt_to_morse(input):
    message = input.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':
  
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
            
  
    return cipher


def morse_to_txt(input):
    message = input
    message += ' '
  
    decipher = ''
    citext = ''
    for letter in message:
  
        # checks for space
        if (letter != ' '):
  
            # counter to keep track of space
            i = 0
  
            # storing morse code of a single character
            citext += letter
  
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
  
            # if i = 2 that indicates a new word
            if i == 2 :
  
                 # adding space to separate words
                decipher += ' '
            else:
  
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
  
    return decipher  

 

@app.route('/', methods = ['GET',  'POST'])
def index():
    return render_template('index.html')

@app.route('/txt', methods = ['GET', 'POST'])
def text():
    if(request.method == 'POST'): 
        input=request.form['input']   
        morse={'morse':txt_to_morse(input)}
        print(txt_to_morse(input))
        return morse
    return render_template('text.html')

@app.route('/morse', methods = ['GET',  'POST'])
def morse():
    if(request.method == 'POST'): 
        input=request.form['input']   
        print(input)
        print(morse_to_txt(input))
        text={'text':morse_to_txt(input)}
        print(text)
        return text
    return render_template('morse.html')    

if __name__ == '__main__':
    app.run(host = 'localhost', port =80)   

    