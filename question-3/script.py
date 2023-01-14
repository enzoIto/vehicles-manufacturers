import csv
import argparse

def detect_delimiter_and_quotechar(file_path):
    with open(file_path, 'r') as file:
        first_line = file.readline()
        return detect_delimiter(first_line), detect_quotechar(first_line)


def detect_delimiter(file_line):
    delimiters = [',','|','\t',';']
    for delimiter in delimiters:
        if delimiter in file_line:
            return delimiter
        else:
            delimiter = '|'
            return delimiter

def detect_quotechar(file_line):
    quotechars = ['"',"'"]
    for quotechar in quotechars:
        if quotechar in file_line:
            return quotechar
        else:
            quotechar = '"'
            return quotechar

def normalize_csv(input_file, output_file, delimiter='|', quotechar='"'):
    delimiter, quotechar = detect_delimiter_and_quotechar(input_file)
    with open(input_file, 'r') as in_file, open(output_file, 'w', newline='') as out_file:
        reader = csv.reader(in_file, delimiter=delimiter, quotechar=quotechar)
        writer = csv.writer(out_file, delimiter=',', quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='The path of the input file')
    parser.add_argument('output_file', help='The path of the output file')
    parser.add_argument('-d', '--delimiter', help='The delimiter used in the input file')
    parser.add_argument('-q', '--quotechar', help='The quote character used in the input file')
    args = parser.parse_args()
    normalize_csv(args.input_file, args.output_file, args.delimiter, args.quotechar)

