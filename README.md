# SwissBorg to Blockpit Converter

This Python script converts transaction data from a SwissBorg CSV file into the format of the Blockpit Manual Import Template CSV file. It combines matching `Sell` and `Buy` transactions into a single `Trade` transaction and also processes `Withdrawal` and `Deposit` transactions.

## Prerequisites

- Python 3.x installed
- Pandas library installed

## Installation

1. **Install Python**

    Download and install the latest version of Python from the official [Python website](https://www.python.org/downloads/).

2. **Install Pandas library**

    Open the Command Prompt and run the following command to install the Pandas library:

    ```sh
    pip install pandas
    ```

## Usage

### SwissBorg Excel-Export as CSV

Save the SwissBorg Excel-Export, which you get from the SwissBorg App and delete row 1 - 13 and save it as CSV-file. Rename it to swissborg_export.csv.

### Download the script

Download the `swissborg_to_blockpit_converter.py` script and save it in a directory of your choice.

### Prepare the CSV files

Ensure that you have the input file `swissborg_export.csv` and the template `blockpit_template.csv` in the same directory as the script.

### Run the script

Open the Command Prompt, navigate to the directory where the script and CSV files are located, and run the script with the following command:

```sh
python swissborg_to_blockpit_converter.py
```

### Check the result

After successfully running the script, a new file `converted_blockpit_import.csv` will be created in the same directory. This file contains the converted transaction data in the Blockpit format.

## Example

Assuming you have the following files in your directory:

- `swissborg_to_blockpit_converter.py`
- `swissborg_export.csv`
- `blockpit_template.csv`

Follow these steps:

1. Open the Command Prompt.
2. Navigate to the directory where the files are located:
    ```sh
    cd path/to/your/directory
    ```
3. Run the script:
    ```sh
    python swissborg_to_blockpit_converter.py
    ```

Check the created file `converted_blockpit_import.csv` in the same directory.

## Troubleshooting

- **Python is not installed:** Ensure that Python is installed and the path to the Python installation is included in the environment variables.
- **Pandas is not installed:** Install the Pandas library with `pip install pandas`.
- **Files not found:** Ensure that the input file and the template are in the same directory as the script and that the file names are correct.