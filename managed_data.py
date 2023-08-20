

import csv
import os

DIRECTORY = "data"
OUTPUT_FILE = "managed_data.csv"

# opening the output_file
with open(OUTPUT_FILE, "w") as output_file:
    writer = csv.writer(output_file)

    # adding a csv header
    header = ["sales", "date", "region"]
    writer.writerow(header)

    # iterating through all files in the data directory
    for file_name in os.listdir(DIRECTORY):
        # opening the csv file for reading
        with open(f"{DIRECTORY}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            # iterating through each row in the csv file
            row_index = 0
            for input_row in reader:
                # if this row is not the csv header, processing now
                if row_index > 0:
                    # collecting data from the row
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    transaction_date = input_row[3]
                    region = input_row[4]

                    # if this is a pink morsel transaction, processing it now
                    if product == "pink morsel":
                        # finishing a formatting data
                        price = float(raw_price[1:])
                        sale = price * int(quantity)

                        # writing the row into our output file
                        output_row = [sale, transaction_date, region]
                        writer.writerow(output_row)
                row_index += 1