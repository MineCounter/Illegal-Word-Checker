#!/bin/bash

# Check if at least one filename is provided as a command-line argument
if [ $# -eq 0 ]; then
  echo "Please provide one or more filenames."
  exit 1
fi

# Specify the words and regex patterns to search for
search_words=("class" "catch" "dict" "match" "pygame" "lambda" "assert" "sys.exit" "raise" "sys.stdin")
regex_patterns=("^\s*print\([^\n]*$" "^\s*open\([^=].*$" "^\s*input\([^=].*$" "^\s*try\s*:")

# Process each file provided as a command-line argument
for file_path in "$@"; do
  # Check if the file exists
  if [ ! -f "$file_path" ]; then
    echo "File not found: $file_path"
    continue
  fi

  echo "Searching in file: $file_path"

  # Record the start time
  start_time=$(date +%s)

  line_number=0
  in_comment=false
  in_docstring=false

  # Read the file line by line and check for the words and regex patterns
  while IFS= read -r line; do
    ((line_number++))

    # Remove single-line comments and inline comments
    line=${line%%#*}

    # Check if we are in a multi-line comment or docstring
    if [[ $line == *"\"\"\""* ]]; then
      if [ "$in_docstring" = true ]; then
        in_docstring=false
      else
        in_docstring=true
      fi
    fi

    # Skip lines in comments or docstrings
    if [ "$in_comment" = true ] || [ "$in_docstring" = true ]; then
      continue
    fi

    # Check for the words in the line
    for word in "${search_words[@]}"; do
      if [[ $line == *"$word"* ]]; then
        echo "Line $line_number: $line"
        break
      fi
    done

    # Check if the line matches any of the regex patterns
    for regex_pattern in "${regex_patterns[@]}"; do
      if [[ $line =~ $regex_pattern ]]; then
        echo "Line $line_number: $line"
        break
      fi
    done

    # Check if we are in a multi-line comment
    if [[ $line == *"#"* ]]; then
      in_comment=true
    fi

    # Check if we have reached the end of a multi-line comment
    if [[ $line == *"#"*"\"\"\""* ]]; then
      in_comment=false
    fi

  done < "$file_path"

  # Record the end time and calculate the elapsed time using integer arithmetic
  end_time=$(date +%s)
  elapsed_time=$((end_time - start_time))

  echo "Search in file $file_path completed in $elapsed_time seconds."

done

echo "Script execution completed."
