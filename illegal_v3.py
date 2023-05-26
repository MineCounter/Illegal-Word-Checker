import sys
import re
import time

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

def insert_word(root, word):
    node = root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_word_end = True

def find_words(root, line):
    matches = []
    words = re.findall(r'\w+', line)
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            if node.is_word_end:
                matches.append(word)
                break
    return matches

# Check if at least one filename is provided as a command-line argument
if len(sys.argv) == 1:
    print("Please provide one or more filenames.")
    sys.exit(1)

# Initialize the Trie root
root = TrieNode()

# Specify the words and regex patterns to search for
search_words = ["class", "catch", "dict", "match", "pygame", "lambda", "assert", "sys.exit", "sys.stdin"]
regex_patterns = [r"^\s*print\([^\n]*$", r"^\s*open\([^=].*$", r"^\s*input\([^=].*$", r"^\s*try\s*:"]

# Insert search words into the Trie
for word in search_words:
    insert_word(root, word)

# Process each file provided as a command-line argument
for file_path in sys.argv[1:]:
    try:
        with open(file_path, 'r') as file:
            print("----------------------------------------(", file_path, ")----------------------------------------\n")

            # Record the start time
            start_time = time.time()

            line_number = 0
            in_comment = False
            in_docstring = False

            # Read the file line by line and check for the words and regex patterns
            for line in file:
                line_number += 1

                # Remove single-line comments and inline comments
                line = line.split('#')[0]

                # Check if we are in a multi-line comment or docstring
                if '"""' in line:
                    if in_docstring:
                        in_docstring = False
                    else:
                        in_docstring = True

                # Skip lines in comments or docstrings
                if in_comment or in_docstring:
                    continue

                # Search for the words in the line
                matches = find_words(root, line)
                if matches:
                    print("Line", line_number, ":", line.strip())
                    print("Matched words:", matches)

                # Check if the line matches any of the regex patterns
                for regex_pattern in regex_patterns:
                    if re.search(regex_pattern, line):
                        print("Line", line_number, ":", line.strip())
                        break

                # Check if we are in a multi-line comment
                if '#' in line:
                    in_comment = True

                # Check if we have reached the end of a multi-line comment
                if '#"""' in line:
                    in_comment = False

            # Record the end time and calculate the elapsed time
            end_time = time.time()
            elapsed_time = end_time - start_time

            print("\nSearch in file", file_path, "completed in", elapsed_time, "seconds.\n")

    except FileNotFoundError:
        print("----------------------------------------(", file_path, ")----------------------------------------\n")
        print("File not found:", file_path, "\n")
        continue

print("----------------------------------( ### Script execution completed ### )----------------------------------\n")
