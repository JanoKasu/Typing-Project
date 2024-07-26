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

def readPDF(path):
    # Get the number of times a monogram or digram appears
    monogram = defaultdict()
    digram = defaultdict()

    # This loop is for the pages
    pdfReader = PyPDF2.PdfReader(path)

    for i in range(1, len(pdfReader.pages)):
        page = pdfReader.pages[i]
        words = page.extract_text().lower()
        # Remove non-ASCII characters from the text
        words = re.sub(r'[^\x61-\x7B,./;]', '', words).split()
        
        # This loop is for the words
        for j in range(len(words)):
            # This loop is for sets of 1 letter (monograms)
            for k in range(len(words[j])):
                di = words[j][k]
                if monogram.__contains__(di):
                    monogram[di] = monogram.get(di) + 1
                else:
                    monogram[di] = 1
            
            # This loop is for sets of 2 letters (digrams)
            for k in range(len(words[j])-1):
                di = words[j][k] + words[j][k+1]
                rev = words[j][k+1] + words[j][k]
                if digram.__contains__(rev):
                    digram[rev] = digram.get(rev) + 1
                elif digram.__contains__(di):
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
        