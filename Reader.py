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

def read_pdf(path):
    try:
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

        # Get the number of times a monogram or digram appears
        # This loop is for the pages
        pdfReader = PyPDF2.PdfReader(path)

        for i in range(len(pdfReader.pages)):
            page = pdfReader.pages[i]
            words = page.extract_text().lower()
            # Remove non-ASCII characters from the text
            words = re.sub(r'[^\x61-\x7A,./;]', '', words).split()
            
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
    except Exception:
        print(Exception.__cause__)

    ##################################################

    # Sort the dictionaries by value (small -> large)

    monogram = sort(monogram)
    digram = sort(digram)

    # Store the data in a json file
    with open("data.json", "w") as outfile:
        grams = { 'monogram' : monogram, 'digram' : digram }
        json.dump(grams, outfile, indent=4 )
        