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
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
            
  
    return cipher


def morse_to_txt(input):
    message = input
    message += ' '
  
    decipher = ''
    citext = ''
    for letter in message:
  
        if (letter != ' '):
  
            i = 0
            citext += letter
  
        else:
            i += 1
  
            if i == 2 :
                decipher += ' '
            else:
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

    