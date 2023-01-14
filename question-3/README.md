# Question 3 

This script reads a CSV file, detects the delimiter and quote character used, and writes the data to a new CSV file using a comma as the delimiter and the detected quote character.

## How to run?

### Arguments

- input_file: path of the input file
- output_file: path of the output file
- -d, --delimiter: The delimiter used in the input file (default: '|')
- -q, --quotechar: The quote character used in the input file (default: '"')

### Usage

```
python normalize_csv.py input_file output_file [-d DELIMITER] [-q QUOTECHAR]
```
### Example

Here are a example of how to run the script:

`python3 script.py csv_file.csv output.csv -d '|'`

this command will run the script with only the delimiter provided, so will use the default quotechar.

To run the other cases, the command-line is similar.

