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

Two graphs will pop up, both of which will be saved as png files in the `images` folder.

### Installing Dependencies
Run `pip install -r Requirements.txt` to install the dependencies needed for this project.

### Customization
You can also add your own text or pdf documents to the appropriate folders under `./PDFs` or `./txts`.

---

Finally, run the data collection algorithm with `python ./Main.py`

## Conclusion
This project is still in development. As of writing, the algorithm to translate the data into a keyboard layout is incomplete.

Note that the project will work with any PDFs or text files in the `files` folder. A good exercise might be to put python or C# code into a text file and see what is generated.

The content in the `files` folder comes from [Project Gutenberg](https://www.gutenberg.org/); a copyright-free repository of e-books.