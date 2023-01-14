import argparse
import csv
import random
import string

parser = argparse.ArgumentParser(description='Generate a CSV file with random data')
parser.add_argument('-r', '--rows', type=int, default=1000000, help='Number of rows to generate')
parser.add_argument('-f', '--file', type=str, default='random_data.csv', help='Filename for the CSV file')
parser.add_argument('-c', '--chunk_size', type=int, default=10000, help='Number of rows per chunk')
args = parser.parse_args()

ROWS = args.rows
COLUMNS = 2
CHUNK_SIZE = args.chunk_size
filename = args.file

# Function to generate a chunk of random data
def generate_data(size):
    data = []
    for i in range(size):
        row = []
        for j in range(COLUMNS):
            if j == 0:
                row.append(random.randint(1000, 9999))
            else:
                row.append(''.join(random.choices(string.ascii_letters, k=10)))
        data.append(row)
    return data

# Write the data to a CSV file in chunks
with open(filename, mode='w') as file:
    writer = csv.writer(file)
    for i in range(0, ROWS, CHUNK_SIZE):
        data = generate_data(CHUNK_SIZE)
        writer.writerows(data)

print(f"generated a CSV file with {ROWS} and {COLUMNS} columns")
