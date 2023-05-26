# Illegal Word Checker

This is a command-line tool written in Python that searches for specific words and regex patterns in one or more files. It utilizes a trie data structure for efficient word matching and regular expressions for pattern matching.

It is made and used for the Computer Science 114 Porject 2023 at Stellenbosch University 

## Usage

1. Clone the repository:

```git clone https://github.com/your-username/file-search-tool.git```


2. Navigate to the project directory:

```cd file-search-tool```


3. Install the required dependencies:

```pip install -r requirements.txt```

csharp


4. Run the tool by providing one or more filenames as command-line arguments:

```python illegal_v3.py file1.py file2.txt```


The tool will search for the specified words and regex patterns in the provided files and display the matching lines along with the matched words.

5. Customize the search words and regex patterns:
6. 

You can modify the `search_words` list and `regex_patterns` list in the `illegal_v3.py` file to suit your specific search requirements. Add or remove words/patterns as needed.

6. File Search Results:

The tool will display the search results in the console. Matched lines will be printed along with the line number and the matched words.

Example output:
```
----------------------------------------( file1.py )----------------------------------------

Line 12: print("Matched line.")
Matched words: ['print']

----------------------------------------( file2.txt )----------------------------------------

Line 5: This line contains the word "example".
Matched words: ['example']

----------------------------------( ### Script execution completed ### )----------------------------------
```

7. Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to submit a pull request.

8. License

This project is licensed under the [MIT License](LICENSE).
