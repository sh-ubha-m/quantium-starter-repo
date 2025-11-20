import csv

# Define the directory containing the CSV files
data_dir = 'data'

# List of CSV file names
csv_files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# List to hold all combined rows
combined_rows = []

# Read data from each CSV file and combine
for csv_file in csv_files:
    file_path = f"{data_dir}/{csv_file}"
    try:
        with open(file_path, 'r') as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0] ==  "pink morsel":
                    combined_rows.append(row)
        print(f"Processed {csv_file}.")
    except FileNotFoundError:
        print(f"File {csv_file} does not exist.")

# Write combined data to sales.csv
with open("sales.csv", 'w', newline='') as new_f:
    print(combined_rows)
    writer = csv.writer(new_f)
    writer.writerow(["Sales","Date","Region"])
    for i in combined_rows:
        print([str(float(i[1][1:])*int(i[2])),i[3],i[4]])
        writer.writerow([str(float(i[1][1:])*int(i[2])),i[3],i[4]])

    

print("Combined data written to sales.csv.")
