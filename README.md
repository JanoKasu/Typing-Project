# Typing Project
## Introduction
This project explores the uses of bigrams in keyboards, and how a keyboard layout can be optimized. Bigrams are combinations of characters, like 'th' and 'he'. Monograms (1 character) are also tracked, but trigrams (3 characters) and larger are not in the scope.

The program does two things; collect data from a folder of text and PDF documents to grab the frequency of the bigrams that appear in them, then perform an algorithm that organizes the bigrams such that a new keyboard layout is provided.

## Running from the Command Line
To get started, open a terminal and create a folder where you will clone this repository to, then clone the repository.

```
cd /your/file/location
mkdir Typing-Project
cd Typing-Project
git clone https://github.com/JanoKasu/Typing-Project.git
```


### Installing Dependencies
#### Instantiate Virtual Environment
Optionally, you can create a virtual environment before installing the requirements. The benefit of doing this is that it avoids polluting your machine with modules you will otherwise never use. Additionally, it's good practice to keep your machine safe. To instantiate a virtual environment, run `python -m venv .\venv`.


Run `pip install -r Requirements.txt` to install the dependencies needed for this project.


### Adding files to read

To run the program, you must first add files to the `files` folder. You can find copyright-free material at [Project Gutenberg](https://www.gutenberg.org/). Alternatively, you can add text files of your code to see what the optimal layout for coding is! The program will return different layouts for different inputs, so try out a variety of genres.

***Note that the files must be .pdf or .txt files to be read.***

```
cd files
explorer .
```

Move the files you want to read into the `files` folder. After adding files, move up one directory, then run the program

```
cd ..
python Main.py
```

Two graphs will pop up, both of which will be saved as png files in the `images` folder. The first is a histogram of the freqencies of bigrams (two letter combinations), and the second is a spring graph showing the relationship of the monograms with each other.


## Conclusion
This project is still in development. As of writing, the algorithm to translate the data into a keyboard layout is incomplete.