<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



  <h3 align="center">Automated Translation Tool</h3>

  <p align="center">
    A lightweight Python-based translation toolkit that supports text translation, file translation, file storage, content reading, and a graphical user interface (GUI).
    <br />
    <a ></a>
    <br />
    <br />
    <a ></a>
  </p>

Features

1. Translate input strings.

2. Translate text files.

3. Save translated text to a file.

4. Read and display text file content.

5. Launch a GUI for interactive translation.





### Built With

Built using MarianMT (Helsinki-NLP opus-mt models).


<!-- GETTING STARTED -->
## Usage

Below are all supported command-line executions.

### 1. Translate a String

Translate a single sentence directly from the command line:
* Translate.py
  ```sh
  python Translate.py "我饿了"
  ```
  
### 2. Translate File and save Translation history

Basic usage (read default path, output to default path):
* TranslateFile.py
  ```sh
  python TranslateFile.py
  ```
  2.1 Specify input file only
* (Default output path will be used)
*   ```sh  
    python TranslateFile.py -i "C:\Users\ericm\Desktop\Myfile\Target.txt"
    ```
     2.2 Specify output directory only
* (Default input path will be used)
*   ```sh  
    python TranslateFile.py -o "D:\Applications\Pycharm Project\MarianMT\Test"
    ```
     2.3 Specify both input and output paths

*   ```sh  
    python TranslateFile.py -i "C:\Users\ericm\Desktop\Myfile\Target.txt" -o "D:\Applications\Pycharm Project\MarianMT\Test"
    ```
### 3. Translate and Read
* Python will read the translated text.
*   ```sh  
    python TranslateFile.py -r True
    ```

### 4. Launch the GUI Translation Window
* This opens an interactive translation tool allowing real-time input and output.
*   ```sh  
    python TranslationGUI.py 
    ```
    
### Default Paths

Default input path:

Set inside TranslateFile.py

Default output path:

Stored and handled by ProcessFile.py

