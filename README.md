# Typing Project
## Introduction
This project explores the uses of bigrams in keyboards, and how a keyboard layout can be optimized. Bigrams are combinations of characters, like 'th' and 'he'. Monograms (1 character) are also tracked, but trigrams (3 characters) and larger are not in the scope.

The program does two things; collect data from a folder of PDFs to grab the frequency of the bigrams that appear in the PDFs, then perform an algorithm that organizes the bigrams such that a new keyboard layout is provided.

## Running from the Command Line
To get started, open a terminal and create a folder where you will clone this repository to, then clone the repository.

```
cd /your/file/location
mkdir Typing-Project
cd Typing-Project
git clone https://github.com/JanoKasu/Typing-Project.git
```

### Installing Dependencies
Run `pip install -r Requirements.txt` to install the dependencies needed for this project.

Finally, run the data collection algorithm with `python ./Main.py`

## Conclusion
This project is still in development. As of writing, the algorithm to translate the data into a keyboard layout is incomplete. 