import csv
from collections import defaultdict

def count_temples_by_location(input_file, output_file):
    temple_counts = defaultdict(int)

    # Read input CSV and count temples by location
    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            location = row['Location'].strip()
            temple_counts[location] += 1

    # Write the counts to a new CSV file
    with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Location', 'Temple Count'])
        for location, count in sorted(temple_counts.items()):
            writer.writerow([location, count])

    print(f"Temple counts written to {output_file}")

def main():
    input_file = 'temple/temples.csv'  # Update with your actual input file path
    output_file = 'temple/temple_counts.csv'  # Output file path
    count_temples_by_location(input_file, output_file)

if __name__ == "__main__":
    main()