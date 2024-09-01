import json
import PyPDF2
import re
import numpy as np
from collections import defaultdict

##################################################

# Takes the full dictionary of a grams as an argument
def sort(grams):
    keys = list(grams.keys())
    values = list(grams.values())
    sorted_value_index = np.argsort(values)
    grams = {keys[i]: values[i] for i in sorted_value_index}
    return grams

##################################################
# Read PDF files

def read_pdf(path):
    try:
        # Get the existing data from the JSON file
        with open("data.json") as f:
            file = json.loads(f.read())
            if "monogram" in file:
                monogram = file["monogram"]
            else:
                monogram = defaultdict()

            if "digram" in file:
                digram = file["digram"]
            else:
                digram = defaultdict()

        # Get the number of times a monogram or digram appears
        # This loop is for the pages
        pdfReader = PyPDF2.PdfReader(path)

        for page in pdfReader.pages:
            words = page.extract_text().lower()
            # Remove non-ASCII characters from the text
            words = re.sub(r'[^\x61-\x7A,./;]', '', words).split()
            
            # This loop is for the words
            for word in words:
                # This loop is for sets of 1 letter (monograms)
                for k in range(len(word)):
                    gram = word[k]
                    if gram in monogram:
                        monogram[gram] = monogram.get(gram) + 1
                    else:
                        monogram[gram] = 1
                
                # This loop is for sets of 2 letters (digrams)
                for char in range(len(word) - 1):
                    di = word[char] + word[char+1]
                    reverse = word[char+1] + word[char]
                    if reverse in digram:
                        digram[reverse] = digram.get(reverse) + 1
                    elif di in digram:
                        digram[di] = digram.get(di) + 1
                    else:
                        digram[di] = 1
    except Exception:
        print(Exception)

    ##################################################
    # Sort the dictionaries by value (small -> large)

    monogram = sort(monogram)
    digram = sort(digram)

    # Store the data in a json file
    with open("data.json", "w") as outfile:
        grams = { 'monogram' : monogram, 'digram' : digram }
        json.dump(grams, outfile, indent=4 )

##################################################
# Read text files

def read_txt(path):
    # Get the existing data from the JSON file
    with open("data.json") as f:
        file = json.loads(f.read())
        if file.__contains__("monogram"):
            monogram = file["monogram"]
        else:
            monogram = defaultdict()

        if file.__contains__("digram"):
            digram = file["digram"]
        else:
            digram = defaultdict()

        with open(path, encoding='UTF-8') as file:
            for line in file:
                words = re.sub(r'[^\x61-\x7A,./;]', '', line.lower()).split()

                for word in words:
                    for char in word:
                        if char in monogram:
                            monogram[char] = monogram.get(char) + 1
                        else:
                            monogram[char] = 1

                    for char in range(len(word) - 1):
                        di = word[char] + word[char+1]
                        reverse = word[char+1] + word[char]
                        
                        if reverse in digram:
                            digram[reverse] = digram.get(reverse) + 1
                        elif di in digram:
                            digram[di] = digram.get(di) + 1
                        else:
                            digram[di] = 1

    ##################################################
    # Sort the dictionaries by value (small -> large)
         
    monogram = sort(monogram)
    digram = sort(digram)

    # Store the data in a json file
    with open("data.json", "w") as outfile:
        grams = { 'monogram' : monogram, 'digram' : digram }
        json.dump(grams, outfile, indent=4 )