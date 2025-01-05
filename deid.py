import re
import pandas as pd


def open_excel(file_path):
    try:
        # Read the Excel file
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def process_row(row):
    # Ensure that row[6] is a string to avoid any errors if it is not
    if isinstance(row[6], str):
        # Convert row[0] and row[1] to strings for replacement
        str_row0 = str(row[0])
        str_row1 = str(row[1])

        # Replace all instances of row[0] with "MRN_REDACT" in row[6]
        row[6] = row[6].replace(str_row0, "MRN_REDACT")

        # Replace all instances of row[1] with "ACCESSION_REDACT" in row[6]
        row[6] = str(row[6]).replace(str_row1, "ACCESSION_REDACT")

        # Replace any DOB
        row[6] = re.sub(r"(DOB:\s*)(\d{1,2}/\d{1,2}/\d{2,4})", r"\1DOB_REDACT", row[6])

        # Replace the "Signed by" part
        row[6] = re.sub(r"(Signed by\s).*?(?=\son\s)", r"\1NAME_REDACT", row[6])

        # Remove Patient Name
        row[6] = re.sub(r"(PATIENT:\s*).*?(?=DOB)", r"\1NAME_REDACT\\n", row[6])
        
        # Remove Referring
        row[6] = re.sub(r"(REFERRING:\s*).*?(?=ATTENDING)", r"\1NAME_REDACT\\n", row[6])
        
        # Remove Attending
        row[6] = re.sub(r"(ATTENDING:\s*).*?(?=RADIOLOGIST)", r"\1NAME_REDACT\\n", row[6])
        
        # Remove Radiologist
        row[6] = re.sub(r"(RADIOLOGIST:\s*).*?(?=ACCESSION_REDACT)", r"\1NAME_REDACT\\n\\n", row[6])

    return row


def process_data(df):
    if df is not None:
        # Convert DataFrame to 2D array (NumPy array)
        data_array = df.to_numpy()

        # Create a new list to store processed rows
        processed_data = []

        # Iterate over the 2D array and process each row        
        for row in data_array:
            processed_row = process_row(row)  # Modify the row in place
            processed_data.append(processed_row)

        # Now that data is processed, create a DataFrame with desired columns
        columns = [
            "MRN",
            "SCAN_ACCESSION",
            "SCAN_TYPE",
            "SCAN_TYPE_CODE",
            "EXAM_DATE",
            "FACILITY",
            "REDACTED_REPORT",
        ]

        # Convert the processed data into a DataFrame
        processed_df = pd.DataFrame(processed_data, columns=columns)

        # Write the processed DataFrame to a new Excel file
        try:
            processed_df.to_excel("output/processed_output.xlsx", index=False)
            print("Processed data written to 'output/processed_output.xlsx'.")
        except Exception as e:
            print(f"An error occurred while writing the file: {e}")

        return processed_df
    else:
        print("No data to process.")
        return None


if __name__ == "__main__":
    # This file path can be changed to whatever the input is!
    file_path = "input.xlsx"
    df = open_excel(file_path)
    processed_df = process_data(df)
